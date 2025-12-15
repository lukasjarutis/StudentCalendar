import json
from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)


class RegisterWindow(QDialog):
    registration_successful = Signal(str)

    def __init__(self, user_file: Path, parent=None):
        super().__init__(parent)

        self.user_file = user_file

        self.setWindowTitle("Registracija")
        self.setModal(True)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        header_label = QLabel("Sukurkite naują paskyrą", self)
        layout.addWidget(header_label)

        form_layout = QFormLayout()
        self.lineEditRegisterUserName = QLineEdit(self)
        self.lineEditRegisterPassword = QLineEdit(self)
        self.lineEditConfirmPassword = QLineEdit(self)

        self.lineEditRegisterPassword.setEchoMode(QLineEdit.Password)
        self.lineEditConfirmPassword.setEchoMode(QLineEdit.Password)

        form_layout.addRow("Naujas vartotojas:", self.lineEditRegisterUserName)
        form_layout.addRow("Naujas slaptažodis:", self.lineEditRegisterPassword)
        form_layout.addRow("Pakartokite slaptažodį:", self.lineEditConfirmPassword)
        layout.addLayout(form_layout)

        self.labelError = QLabel("", self)
        layout.addWidget(self.labelError)

        buttons_layout = QHBoxLayout()
        self.buttonRegister = QPushButton("Registruotis", self)
        self.buttonCancel = QPushButton("Atšaukti", self)
        buttons_layout.addWidget(self.buttonRegister)
        buttons_layout.addWidget(self.buttonCancel)
        layout.addLayout(buttons_layout)

        self.buttonRegister.clicked.connect(self.handle_register)
        self.buttonCancel.clicked.connect(self.reject)

    def handle_register(self):
        username = self.lineEditRegisterUserName.text().strip()
        password = self.lineEditRegisterPassword.text().strip()
        confirm_password = self.lineEditConfirmPassword.text().strip()

        if not username or not password or not confirm_password:
            self.show_error("Užpildykite visus registracijos laukus")
            return

        if password != confirm_password:
            self.show_error("Slaptažodžiai nesutampa")
            return

        users = self.load_users()
        if username in users:
            self.show_error("Toks vartotojas jau egzistuoja")
            return

        users[username] = password
        self.save_users(users)
        self.registration_successful.emit(username)
        QMessageBox.information(self, "Sėkmė", "Vartotojas sėkmingai užregistruotas")
        self.accept()

    def load_users(self):
        if self.user_file.exists():
            try:
                with open(self.user_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict):
                    return {str(k): str(v) for k, v in data.items()}
            except json.JSONDecodeError:
                return {}
        return {}

    def save_users(self, users: dict):
        with open(self.user_file, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

    def show_error(self, message: str):
        self.labelError.setText(message)

