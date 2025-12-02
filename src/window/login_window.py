from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit
from src.window.ui_login_window import Ui_dialogLogin
from src.window.main_window import MainWindow


class LoginWindow(QDialog, Ui_dialogLogin):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        if isinstance(self.findChild(QLineEdit, "lineEditPassword"), QLineEdit):
            self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.buttonLogin.clicked.connect(self.handle_login)

        if hasattr(self, "buttonCancel"):
            self.buttonCancel.clicked.connect(self.close)

        if hasattr(self, "labelError"):
            self.labelError.setText("")

    def handle_login(self):
        username = self.lineEditUserName.text().strip()
        password = self.lineEditUserPassword.text().strip()

        if username == "student" and password == "1234":
            self.open_main_window()
        else:
            if hasattr(self, "labelError"):
                self.labelError.setText("Neteisingi prisijungimo duomenys")
            else:
                QMessageBox.warning(self, "Klaida", "Neteisingi prisijungimo duomenys")

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()
