from PySide6.QtGui import QColor, QPalette


def apply_dark_blue_theme(app):
    """Apply a dark/light blue color palette and stylesheet to the whole app."""

    dark_base = QColor("#0b1d3a")
    panel = QColor("#1a2f5a")
    text_color = QColor("#e6f2ff")

    palette = QPalette()
    palette.setColor(QPalette.Window, dark_base)
    palette.setColor(QPalette.WindowText, text_color)
    palette.setColor(QPalette.Base, panel)
    palette.setColor(QPalette.AlternateBase, QColor("#142b50"))
    palette.setColor(QPalette.ToolTipBase, panel)
    palette.setColor(QPalette.ToolTipText, text_color)
    palette.setColor(QPalette.Text, text_color)
    palette.setColor(QPalette.Button, QColor("#1f3f70"))
    palette.setColor(QPalette.ButtonText, text_color)
    palette.setColor(QPalette.Highlight, QColor("#28518f"))
    palette.setColor(QPalette.HighlightedText, text_color)

    app.setPalette(palette)

    app.setStyleSheet(
        """
        QWidget {
            background-color: #0b1d3a;
            color: #e6f2ff;
            selection-background-color: #28518f;
            selection-color: #e6f2ff;
        }

        QLabel {
            color: #e6f2ff;
        }

        QLineEdit, QSpinBox, QComboBox, QTextEdit, QPlainTextEdit, QListWidget, QTableWidget, QTreeWidget {
            background-color: #1a2f5a;
            border: 1px solid #4da3ff;
            border-radius: 4px;
            color: #e6f2ff;
            selection-background-color: #28518f;
            selection-color: #e6f2ff;
        }

        QTableWidget {
            gridline-color: #4da3ff;
            alternate-background-color: #142b50;
        }

        QHeaderView::section {
            background-color: #1f3f70;
            color: #e6f2ff;
            border: 1px solid #4da3ff;
            padding: 4px;
        }

        QPushButton {
            background-color: #1f3f70;
            color: #e6f2ff;
            border: 1px solid #4da3ff;
            padding: 6px 10px;
            border-radius: 6px;
        }

        QPushButton:hover {
            background-color: #28518f;
        }

        QPushButton:pressed {
            background-color: #1a3b73;
        }

        QMenuBar, QMenu {
            background-color: #1f3f70;
            color: #e6f2ff;
        }

        QMenu::item:selected {
            background-color: #28518f;
        }
        """
    )
