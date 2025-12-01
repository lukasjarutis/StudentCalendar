import sys
from PyQt5.QtWidgets import QApplication, QDialog

from window.login_window import LoginWindow
from window.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    login_dialog = LoginWindow()

    if login_dialog.exec_() == QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
