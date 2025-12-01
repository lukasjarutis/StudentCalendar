from PyQt5.QtWidgets import (
    QDialog, QLineEdit, QLabel, QPushButton,
    QVBoxLayout, QFormLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Prisijungimas")
        self.resize(350, 180)
        self.setModal(True)

        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        form_layout = QFormLayout()
        form_layout.addRow("Login:", self.username_edit)
        form_layout.addRow("Password:", self.password_edit)

        self.login_button = QPushButton("Sign up")
        self.cancel_button = QPushButton("Cancel")

        self.login_button.clicked.connect(self.on_login)
        self.cancel_button.clicked.connect(self.reject)

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.login_button)
        buttons_layout.addWidget(self.cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def on_login(self):
        username = self.username_edit.text().strip()
        password = self.password_edit.text().strip()

        if username == "" and password == "":
            self.accept()
        else:
            QMessageBox.warning(
                self,
                "Error!",
                "Wrong login or password.",
                QMessageBox.Ok,
                QMessageBox.Ok
            )