import sys

from PySide6.QtWidgets import QApplication
from src.window.login_window import LoginWindow
from src.theme import apply_dark_blue_theme


if __name__ == "__main__":
    app = QApplication(sys.argv)

    apply_dark_blue_theme(app)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())
