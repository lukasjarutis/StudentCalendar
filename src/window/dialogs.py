from PySide6.QtWidgets import (
    QDialog, QLineEdit, QTextEdit, QFormLayout,
    QPushButton, QHBoxLayout, QVBoxLayout,
    QLabel, QCheckBox, QGroupBox, QGridLayout, QComboBox)
from PySide6.QtCore import Qt


class LessonDialog(QDialog):
    def __init__(self, parent=None, subject="", room="", teacher="", notes="", lesson_type="", exam=False):
        super().__init__(parent)

        self.setWindowTitle("Paskaitos redagavimas")
        self.resize(350, 300)

        self.subject_edit = QLineEdit(subject)
        self.type_edit = QLineEdit(lesson_type)
        self.room_edit = QLineEdit(room)
        self.teacher_edit = QLineEdit(teacher)
        self.notes_edit = QTextEdit(notes)
        self.exam_checkbox = QCheckBox("Yra įskaita / egzaminas")
        self.exam_checkbox.setChecked(bool(exam))

        form_layout = QFormLayout()
        form_layout.addRow("Dalykas:", self.subject_edit)
        form_layout.addRow("Tipas:", self.type_edit)
        form_layout.addRow("Auditorija:", self.room_edit)
        form_layout.addRow("Dėstytojas:", self.teacher_edit)
        form_layout.addRow("Pastabos:", self.notes_edit)
        form_layout.addRow("Įskaita / egzaminas:", self.exam_checkbox)

        ok_button = QPushButton("Išsaugoti")
        cancel_button = QPushButton("Atšaukti")

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(ok_button)
        buttons_layout.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def get_data(self):
        return {
            "subject": self.subject_edit.text().strip(),
            "type": self.type_edit.text().strip(),
            "room": self.room_edit.text().strip(),
            "teacher": self.teacher_edit.text().strip(),
            "notes": self.notes_edit.toPlainText().strip(),
            "exam": self.exam_checkbox.isChecked(),
        }


class GlobalSubjectDialog(QDialog):
    def __init__(self, parent, day_names, time_slots):
        super().__init__(parent)

        self.day_names = day_names
        self.time_slots = time_slots
        self.checkboxes = {}

        self.setWindowTitle("Naujas dalykas")
        self.resize(700, 500)

        self.subject_edit = QLineEdit()
        self.type_edit = QLineEdit()
        self.room_edit = QLineEdit()
        self.teacher_edit = QLineEdit()
        self.notes_edit = QTextEdit()
        self.exam_checkbox = QCheckBox("Yra įskaita / egzaminas")

        self.repeat_combo = QComboBox()
        self.repeat_combo.addItem("Kiekvieną savaitę", "weekly")
        self.repeat_combo.addItem("Kas antrą savaitę", "biweekly")

        form_layout = QFormLayout()
        form_layout.addRow("Dalykas:", self.subject_edit)
        form_layout.addRow("Tipas:", self.type_edit)
        form_layout.addRow("Auditorija:", self.room_edit)
        form_layout.addRow("Dėstytojas:", self.teacher_edit)
        form_layout.addRow("Pastabos:", self.notes_edit)
        form_layout.addRow("Įskaita / egzaminas:", self.exam_checkbox)
        form_layout.addRow("Pasikartojimas:", self.repeat_combo)

        grid_layout = QGridLayout()
        grid_layout.addWidget(QLabel("Laikas / Diena"), 0, 0)

        for col, day in enumerate(self.day_names):
            lbl = QLabel(day)
            lbl.setAlignment(Qt.AlignCenter)
            grid_layout.addWidget(lbl, 0, col + 1)

        for row, time_str in enumerate(self.time_slots):
            time_label = QLabel(time_str)
            grid_layout.addWidget(time_label, row + 1, 0)

            for col in range(len(self.day_names)):
                cb = QCheckBox()
                self.checkboxes[(row, col)] = cb
                grid_layout.addWidget(cb, row + 1, col + 1)

        grid_group = QGroupBox("Kada vyksta paskaita?")
        grid_group.setLayout(grid_layout)

        ok_button = QPushButton("Pridėti")
        cancel_button = QPushButton("Atšaukti")
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(ok_button)
        buttons_layout.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(grid_group)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def get_data(self):
        cells = [
            (row, col)
            for (row, col), cb in self.checkboxes.items()
            if cb.isChecked()
        ]

        return {
            "subject": self.subject_edit.text().strip(),
            "type": self.type_edit.text().strip(),
            "room": self.room_edit.text().strip(),
            "teacher": self.teacher_edit.text().strip(),
            "notes": self.notes_edit.toPlainText().strip(),
            "exam": self.exam_checkbox.isChecked(),
            "repeat": self.repeat_combo.currentData(),
            "cells": cells,
        }