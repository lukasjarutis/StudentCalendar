import json
from pathlib import Path

from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit
from src.window.ui_login_window import Ui_dialogLogin
from src.window.main_window import MainWindow
from src.window.register_window import RegisterWindow


class LoginWindow(QDialog, Ui_dialogLogin):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.user_file = Path(__file__).resolve().parents[1] / "users.json"

        if isinstance(self.findChild(QLineEdit, "lineEditUserPassword"), QLineEdit):
            self.lineEditUserPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.buttonLogin.clicked.connect(self.handle_login)
        if hasattr(self, "buttonOpenRegister"):
            self.buttonOpenRegister.clicked.connect(self.open_register_window)

        if hasattr(self, "buttonCancel"):
            self.buttonCancel.clicked.connect(self.close)

        if hasattr(self, "labelError"):
            self.labelError.setText("")

    def handle_login(self):
        username = self.lineEditUserName.text().strip()
        password = self.lineEditUserPassword.text().strip()

        users = self.load_users()

        if username in users and password == users[username]:
            self.open_main_window()
        elif username == "student" and password == "1234":
            self.open_main_window()
        else:
            self.show_error("Neteisingi prisijungimo duomenys")

    def open_register_window(self):
        self.register_window = RegisterWindow(self.user_file, self)
        self.register_window.registration_successful.connect(self.show_registration_success)
        self.register_window.exec()

    def show_registration_success(self, username: str):
        if hasattr(self, "labelError"):
            self.labelError.setText(f"Vartotojas '{username}' sėkmingai užregistruotas")

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

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
        if hasattr(self, "labelError"):
            self.labelError.setText(message)
        else:
            QMessageBox.warning(self, "Klaida", message)
