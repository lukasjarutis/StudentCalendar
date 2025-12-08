from datetime import date, timedelta

from PySide6.QtWidgets import (
    QMainWindow, QTableWidgetItem, QFileDialog, QMessageBox, QHeaderView, QDialog
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QGuiApplication, QColor

from src.window.ui_main_window import Ui_MainWindow
from src.window.dialogs import LessonDialog, GlobalSubjectDialog
from src.window.schedule_modul import ScheduleModel
from src.config import TIME_SLOTS, DAY_NAMES, DEFAULT_FILENAME
from src.utils import format_lesson_text
from src.storage import save_schedule, load_schedule


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("Studento kalendorius")
        self.default_filename = DEFAULT_FILENAME

        self.model = ScheduleModel()

        self.time_slots = TIME_SLOTS
        self.day_names = DAY_NAMES

        screen = QGuiApplication.primaryScreen()
        available = screen.availableGeometry()
        width = int(available.width() * 0.8)
        height = int(available.height() * 0.8)
        self.setMinimumSize(1200, 700)
        self.resize(width, height)

        today = date.today()
        self.current_monday = today - timedelta(days=today.weekday())

        self.pushBtnAddSub.clicked.connect(self.add_subject_globally)
        self.pushBtnPrevWeek.clicked.connect(lambda: self.change_week(-1))
        self.pushBtnNextWeek.clicked.connect(lambda: self.change_week(1))

        if hasattr(self, "actionSave") and isinstance(self.actionSave, QAction):
            self.actionSave.triggered.connect(self.save_to_file_dialog)
        if hasattr(self, "actionLoad") and isinstance(self.actionLoad, QAction):
            self.actionLoad.triggered.connect(self.load_from_file_dialog)

        self.setup_table()

        try:
            load_schedule(self.default_filename, self.model)
        except FileNotFoundError:
            pass
        except Exception:
            pass

        self.update_week_view()

    def setup_table(self):
        table = self.tableSchedule

        table.setRowCount(len(self.time_slots))
        table.setColumnCount(len(self.day_names))

        table.setVerticalHeaderLabels(self.time_slots)

        header_h = table.horizontalHeader()
        header_v = table.verticalHeader()
        header_h.setSectionResizeMode(QHeaderView.Stretch)
        header_v.setSectionResizeMode(QHeaderView.Stretch)

        table.setWordWrap(True)
        table.cellDoubleClicked.connect(self.edit_lesson)

    def change_week(self, delta_weeks: int):
        self.current_monday += timedelta(weeks=delta_weeks)
        self.update_week_view()

    def _make_item_from_data(self, data):
        text = format_lesson_text(data)
        if data.get("exam"):
            if text:
                text = "❗\n" + text
            else:
                text = "❗"

        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        item.setData(Qt.UserRole, data)

        if data.get("exam"):
            item.setForeground(QColor(Qt.red))

        return item

    def update_week_view(self):
        self.week_dates = [
            self.current_monday + timedelta(days=i) for i in range(len(self.day_names))
        ]

        week_start = self.week_dates[0]
        week_end = self.week_dates[-1]
        self.labelCurrentWeek.setText(
            f"{week_start.strftime('%Y-%m-%d')} – {week_end.strftime('%Y-%m-%d')}"
        )

        headers = []
        for day_name, d in zip(self.day_names, self.week_dates):
            headers.append(f"{day_name}\n{d.strftime('%Y-%m-%d')}")
        self.tableSchedule.setHorizontalHeaderLabels(headers)

        self.tableSchedule.clearContents()

        grid = self.model.build_week_cells(
            self.current_monday,
            len(self.day_names),
            len(self.time_slots),
        )

        for row in range(len(self.time_slots)):
            for col in range(len(self.day_names)):
                data = grid[row][col]
                if not data:
                    continue

                item = self._make_item_from_data(data)
                self.tableSchedule.setItem(row, col, item)

    def edit_lesson(self, row, column):
        day_date = self.week_dates[column]
        iso = day_date.isoformat()

        existing = self.model.get_single_lesson(iso, row) or {}

        dialog = LessonDialog(
            self,
            subject=existing.get("subject", ""),
            room=existing.get("room", ""),
            teacher=existing.get("teacher", ""),
            notes=existing.get("notes", ""),
            lesson_type=existing.get("type", ""),
            exam=existing.get("exam", False),
        )

        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()

            print("DEBUG LESSON DATA:", data)

            if not data["subject"]:
                self.model.remove_single_lesson(iso, row)
                self.tableSchedule.setItem(row, column, QTableWidgetItem(""))
                return

            self.model.set_single_lesson(iso, row, data)

            item = self._make_item_from_data(data)
            self.tableSchedule.setItem(row, column, item)

    def add_subject_globally(self):
        dialog = GlobalSubjectDialog(self, self.day_names, self.time_slots)

        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()

            subject = data["subject"]
            cells = data["cells"]
            repeat = data["repeat"]

            if not subject or not cells:
                return

            for row, col in cells:
                self.model.add_recurring_lesson(
                    weekday=col,
                    row=row,
                    repeat=repeat,
                    base_monday=self.current_monday,
                    subject=subject,
                    type_=data["type"],
                    room=data["room"],
                    teacher=data["teacher"],
                    notes=data["notes"],
                    exam=data["exam"],
                )

            self.update_week_view()

    def save_to_file_dialog(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Išsaugoti tvarkaraštį",
            self.default_filename,
            "JSON failai (*.json);;Visi failai (*)",
        )
        if not path:
            return
        self.default_filename = path
        try:
            save_schedule(path, self.model)
            QMessageBox.information(self, "Išsaugota", f"Tvarkaraštis išsaugotas į:\n{path}")
        except Exception as e:
            QMessageBox.critical(self, "Klaida", f"Nepavyko išsaugoti failo:\n{e}")

    def load_from_file_dialog(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Atidaryti tvarkaraštį",
            "",
            "JSON failai (*.json);;Visi failai (*)",
        )
        if not path:
            return
        self.default_filename = path
        try:
            load_schedule(path, self.model)
            QMessageBox.information(self, "Atidaryta", f"Tvarkaraštis įkeltas iš:\n{path}")
            self.update_week_view()
        except FileNotFoundError:
            QMessageBox.warning(self, "Klaida", "Failas nerastas.")
        except Exception as e:
            QMessageBox.critical(self, "Klaida", f"Nepavyko nuskaityti failo:\n{e}")
