from PySide6.QtWidgets import QHBoxLayout, QPushButton, QLabel, QWidget
from PySide6.QtCore import Qt


def create_toolbar(window):
    nav_layout = QHBoxLayout()

    window.add_subject_button = QPushButton("➕ Pridėti dalyką")
    window.add_subject_button.clicked.connect(window.add_subject_globally)
    nav_layout.addWidget(window.add_subject_button)

    center_layout = QHBoxLayout()
    window.prev_week_button = QPushButton("← Ankstesnė savaitė")
    window.next_week_button = QPushButton("Kita savaitė →")
    window.week_label = QLabel()
    window.week_label.setAlignment(Qt.AlignCenter)

    window.prev_week_button.clicked.connect(lambda: window.change_week(-1))
    window.next_week_button.clicked.connect(lambda: window.change_week(1))

    center_layout.addWidget(window.prev_week_button)
    center_layout.addWidget(window.week_label)
    center_layout.addWidget(window.next_week_button)

    center_widget = QWidget()
    center_widget.setLayout(center_layout)
    nav_layout.addWidget(center_widget, alignment=Qt.AlignCenter)

    window.share_button = QPushButton("Share")
    nav_layout.addWidget(window.share_button)

    return nav_layout