# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        self.actionSaveFile = QAction(MainWindow)
        self.actionSaveFile.setObjectName(u"actionSaveFile")
        self.actionOpenFile = QAction(MainWindow)
        self.actionOpenFile.setObjectName(u"actionOpenFile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLocale(QLocale(QLocale.Lithuanian, QLocale.Lithuania))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setWeight(QFont.ExtraBold)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.widgetCentralControl = QWidget(self.centralwidget)
        self.widgetCentralControl.setObjectName(u"widgetCentralControl")
        self.horizontalLayout = QHBoxLayout(self.widgetCentralControl)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushBtnAddSub = QPushButton(self.widgetCentralControl)
        self.pushBtnAddSub.setObjectName(u"pushBtnAddSub")

        self.horizontalLayout.addWidget(self.pushBtnAddSub)

        self.widgetWeeksControl = QWidget(self.widgetCentralControl)
        self.widgetWeeksControl.setObjectName(u"widgetWeeksControl")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetWeeksControl)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushBtnPrevWeek = QPushButton(self.widgetWeeksControl)
        self.pushBtnPrevWeek.setObjectName(u"pushBtnPrevWeek")

        self.horizontalLayout_2.addWidget(self.pushBtnPrevWeek)

        self.labelCurrentWeek = QLabel(self.widgetWeeksControl)
        self.labelCurrentWeek.setObjectName(u"labelCurrentWeek")
        self.labelCurrentWeek.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelCurrentWeek.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.labelCurrentWeek)

        self.pushBtnNextWeek = QPushButton(self.widgetWeeksControl)
        self.pushBtnNextWeek.setObjectName(u"pushBtnNextWeek")

        self.horizontalLayout_2.addWidget(self.pushBtnNextWeek)


        self.horizontalLayout.addWidget(self.widgetWeeksControl)

        self.pushBtnShare = QPushButton(self.widgetCentralControl)
        self.pushBtnShare.setObjectName(u"pushBtnShare")

        self.horizontalLayout.addWidget(self.pushBtnShare)


        self.verticalLayout.addWidget(self.widgetCentralControl)

        self.tableSchedule = QTableWidget(self.centralwidget)
        self.tableSchedule.setObjectName(u"tableSchedule")

        self.verticalLayout.addWidget(self.tableSchedule)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSaveFile)
        self.menuFile.addAction(self.actionOpenFile)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSaveFile.setText(QCoreApplication.translate("MainWindow", u"I\u0161saugoti", None))
        self.actionOpenFile.setText(QCoreApplication.translate("MainWindow", u"Atidaryti", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Savait\u0117s tvarkara\u0161tis", None))
        self.pushBtnAddSub.setText(QCoreApplication.translate("MainWindow", u"\u2795 Prid\u0117ti dalyk\u0105", None))
        self.pushBtnPrevWeek.setText(QCoreApplication.translate("MainWindow", u"\u2190 Ankstesn\u0117 savait\u0117", None))
        self.labelCurrentWeek.setText("")
        self.pushBtnNextWeek.setText(QCoreApplication.translate("MainWindow", u"Kita savait\u0117 \u2192", None))
        self.pushBtnShare.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

