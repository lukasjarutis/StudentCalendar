from PySide6.QtWidgets import QDialog, QCheckBox, QLabel
from PySide6.QtCore import Qt

from .ui_lesson_dialog import Ui_LessonDialog
from .ui_global_subject_dialog import Ui_GlobalSubjectDialog


class LessonDialog(QDialog, Ui_LessonDialog):
    def __init__(self, parent=None, subject="", room="", teacher="", notes="", lesson_type="", exam=False):
        super().__init__(parent)
        self.setupUi(self)

        self.subjectEdit.setText(subject)
        self.typeEdit.setText(lesson_type)
        self.roomEdit.setText(room)
        self.teacherEdit.setText(teacher)
        self.notesEdit.setPlainText(notes)
        self.examCheckBox.setChecked(bool(exam))

        self.buttonOk.clicked.connect(self.accept)
        self.buttonCancel.clicked.connect(self.reject)

    def get_data(self):
        return {
            "subject": self.subjectEdit.text().strip(),
            "type": self.typeEdit.text().strip(),
            "room": self.roomEdit.text().strip(),
            "teacher": self.teacherEdit.text().strip(),
            "notes": self.notesEdit.toPlainText().strip(),
            "exam": self.examCheckBox.isChecked(),
        }


class GlobalSubjectDialog(QDialog, Ui_GlobalSubjectDialog):
    def __init__(self, parent, day_names, time_slots):
        super().__init__(parent)
        self.setupUi(self)

        self.day_names = day_names
        self.time_slots = time_slots
        self.checkboxes = {}

        self.repeatCombo.clear()
        self.repeatCombo.addItem("Kiekvieną savaitę", "weekly")
        self.repeatCombo.addItem("Kas antrą savaitę", "biweekly")

        self._build_grid()

        self.buttonOk.clicked.connect(self.accept)
        self.buttonCancel.clicked.connect(self.reject)

    def _build_grid(self):
        layout = self.gridLayoutLessons

        header_label = QLabel("Laikas / Diena")
        layout.addWidget(header_label, 0, 0)

        for col, day in enumerate(self.day_names):
            lbl = QLabel(day)
            lbl.setAlignment(Qt.AlignCenter)
            layout.addWidget(lbl, 0, col + 1)

        for row, time_str in enumerate(self.time_slots):
            time_label = QLabel(time_str)
            layout.addWidget(time_label, row + 1, 0)

            for col in range(len(self.day_names)):
                cb = QCheckBox()
                self.checkboxes[(row, col)] = cb
                layout.addWidget(cb, row + 1, col + 1)

    def get_data(self):
        cells = [
            (row, col)
            for (row, col), cb in self.checkboxes.items()
            if cb.isChecked()
        ]

        return {
            "subject": self.subjectEdit.text().strip(),
            "type": self.typeEdit.text().strip(),
            "room": self.roomEdit.text().strip(),
            "teacher": self.teacherEdit.text().strip(),
            "notes": self.notesEdit.toPlainText().strip(),
            "exam": self.examCheckBox.isChecked(),
            "repeat": self.repeatCombo.currentData(),
            "cells": cells,
        }