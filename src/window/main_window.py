from datetime import date, timedelta

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QFileDialog, QMessageBox, QAction
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication, QColor

from src.window.dialogs import LessonDialog, GlobalSubjectDialog
from src.window.schedule_modul import ScheduleModel
from src.config import TIME_SLOTS, DAY_NAMES, DEFAULT_FILENAME
from src.utils import format_lesson_text
from src.storage import save_schedule, load_schedule
from src.window.toolbar import create_toolbar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Studento kalendorius")
        self.default_filename = DEFAULT_FILENAME

        screen = QGuiApplication.primaryScreen()
        available = screen.availableGeometry()
        width = int(available.width() * 0.8)
        height = int(available.height() * 0.8)
        self.setMinimumSize(1200, 700)
        self.resize(width, height)

        self.model = ScheduleModel()

        self.time_slots = TIME_SLOTS
        self.day_names = DAY_NAMES

        today = date.today()
        self.current_monday = today - timedelta(days=today.weekday())

        self.create_menus()

        central_widget = QWidget()
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        title_label = QLabel("Savaitės tvarkaraštis")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.main_layout.addWidget(title_label)

        toolbar_layout = create_toolbar(self)
        self.main_layout.addLayout(toolbar_layout)

        self.setup_table()
        self.main_layout.addWidget(self.table)

        self.setCentralWidget(central_widget)

        try:
            load_schedule(self.default_filename, self.model)
        except FileNotFoundError:
            pass
        except Exception:
            pass

        self.update_week_view()

    def create_menus(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Failas")

        save_action = QAction("Išsaugoti...", self)
        save_action.triggered.connect(self.save_to_file_dialog)
        file_menu.addAction(save_action)

        load_action = QAction("Atidaryti...", self)
        load_action.triggered.connect(self.load_from_file_dialog)
        file_menu.addAction(load_action)

    def setup_table(self):
        self.table = QTableWidget(len(self.time_slots), len(self.day_names), self)
        self.table.setVerticalHeaderLabels(self.time_slots)

        header_h = self.table.horizontalHeader()
        header_v = self.table.verticalHeader()
        header_h.setSectionResizeMode(QHeaderView.Stretch)
        header_v.setSectionResizeMode(QHeaderView.Stretch)

        self.table.setWordWrap(True)
        self.table.cellDoubleClicked.connect(self.edit_lesson)

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
        self.week_label.setText(
            f"Savaitė: {week_start.strftime('%Y-%m-%d')} – {week_end.strftime('%Y-%m-%d')}"
        )

        headers = []
        for day_name, d in zip(self.day_names, self.week_dates):
            headers.append(f"{day_name}\n{d.strftime('%Y-%m-%d')}")
        self.table.setHorizontalHeaderLabels(headers)

        self.table.clearContents()

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
                self.table.setItem(row, col, item)

    def edit_lesson(self, row, column):
        day_date = self.week_dates[column]
        iso = day_date.isoformat()

        existing = self.model.get_single_lesson(iso, row) or {}

        dialog = LessonDialog(
            self,
            subject=existing.get("subject", ""),
            lesson_type=existing.get("type", ""),
            room=existing.get("room", ""),
            teacher=existing.get("teacher", ""),
            notes=existing.get("notes", ""),
            exam=existing.get("exam", False),
        )

        if dialog.exec_() == dialog.Accepted:
            data = dialog.get_data()

            if not data["subject"]:
                self.model.remove_single_lesson(iso, row)
                self.table.setItem(row, column, QTableWidgetItem(""))
                return

            self.model.set_single_lesson(iso, row, data)

            item = self._make_item_from_data(data)
            self.table.setItem(row, column, item)

    def add_subject_globally(self):
        dialog = GlobalSubjectDialog(self, self.day_names, self.time_slots)

        if dialog.exec_() == dialog.Accepted:
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
