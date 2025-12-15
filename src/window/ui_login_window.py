# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QLocale,
                            QMetaObject, QRect)
from PySide6.QtWidgets import (QLabel, QLineEdit,
                               QPushButton)

class Ui_dialogLogin(object):
    def setupUi(self, dialogLogin):
        if not dialogLogin.objectName():
            dialogLogin.setObjectName(u"dialogLogin")
        dialogLogin.resize(300, 460)
        self.labelUsername = QLabel(dialogLogin)
        self.labelUsername.setObjectName(u"labelUsername")
        self.labelUsername.setEnabled(True)
        self.labelUsername.setGeometry(QRect(75, 50, 150, 16))
        self.labelUsername.setLocale(QLocale(QLocale.Lithuanian, QLocale.Lithuania))
        self.labelUserPassword = QLabel(dialogLogin)
        self.labelUserPassword.setObjectName(u"labelUserPassword")
        self.labelUserPassword.setGeometry(QRect(75, 110, 150, 16))
        self.labelUserPassword.setLocale(QLocale(QLocale.Lithuanian, QLocale.Lithuania))
        self.lineEditUserName = QLineEdit(dialogLogin)
        self.lineEditUserName.setObjectName(u"lineEditUserName")
        self.lineEditUserName.setGeometry(QRect(75, 70, 150, 21))
        self.lineEditUserPassword = QLineEdit(dialogLogin)
        self.lineEditUserPassword.setObjectName(u"lineEditUserPassword")
        self.lineEditUserPassword.setGeometry(QRect(75, 130, 150, 21))
        self.lineEditUserPassword.setEchoMode(QLineEdit.Password)
        self.buttonLogin = QPushButton(dialogLogin)
        self.buttonLogin.setObjectName(u"buttonLogin")
        self.buttonLogin.setGeometry(QRect(60, 200, 80, 27))
        self.buttonCancel = QPushButton(dialogLogin)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(160, 200, 80, 27))
        self.labelError = QLabel(dialogLogin)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setGeometry(QRect(75, 170, 150, 16))
        self.labelError.setLocale(QLocale(QLocale.Lithuanian, QLocale.Lithuania))
        self.labelRegisterHeader = QLabel(dialogLogin)
        self.labelRegisterHeader.setObjectName(u"labelRegisterHeader")
        self.labelRegisterHeader.setGeometry(QRect(75, 230, 150, 16))
        self.labelRegisterUsername = QLabel(dialogLogin)
        self.labelRegisterUsername.setObjectName(u"labelRegisterUsername")
        self.labelRegisterUsername.setGeometry(QRect(75, 260, 150, 16))
        self.lineEditRegisterUserName = QLineEdit(dialogLogin)
        self.lineEditRegisterUserName.setObjectName(u"lineEditRegisterUserName")
        self.lineEditRegisterUserName.setGeometry(QRect(75, 280, 150, 21))
        self.labelRegisterPassword = QLabel(dialogLogin)
        self.labelRegisterPassword.setObjectName(u"labelRegisterPassword")
        self.labelRegisterPassword.setGeometry(QRect(75, 320, 150, 16))
        self.lineEditRegisterPassword = QLineEdit(dialogLogin)
        self.lineEditRegisterPassword.setObjectName(u"lineEditRegisterPassword")
        self.lineEditRegisterPassword.setGeometry(QRect(75, 340, 150, 21))
        self.lineEditRegisterPassword.setEchoMode(QLineEdit.Password)
        self.labelConfirmPassword = QLabel(dialogLogin)
        self.labelConfirmPassword.setObjectName(u"labelConfirmPassword")
        self.labelConfirmPassword.setGeometry(QRect(75, 380, 150, 16))
        self.lineEditConfirmPassword = QLineEdit(dialogLogin)
        self.lineEditConfirmPassword.setObjectName(u"lineEditConfirmPassword")
        self.lineEditConfirmPassword.setGeometry(QRect(75, 400, 150, 21))
        self.lineEditConfirmPassword.setEchoMode(QLineEdit.Password)
        self.buttonRegister = QPushButton(dialogLogin)
        self.buttonRegister.setObjectName(u"buttonRegister")
        self.buttonRegister.setGeometry(QRect(100, 430, 101, 27))

        self.retranslateUi(dialogLogin)

        QMetaObject.connectSlotsByName(dialogLogin)
    # setupUi

    def retranslateUi(self, dialogLogin):
        dialogLogin.setWindowTitle(QCoreApplication.translate("dialogLogin", u"Dialog", None))
        self.labelUsername.setText(QCoreApplication.translate("dialogLogin", u"Vartotojo vardas:", None))
        self.labelUserPassword.setText(QCoreApplication.translate("dialogLogin", u"Slapta\u017eodis:", None))
        self.buttonLogin.setText(QCoreApplication.translate("dialogLogin", u"Prisijungti", None))
        self.buttonCancel.setText(QCoreApplication.translate("dialogLogin", u"At\u0161aukti", None))
        self.labelError.setText("")
        self.labelRegisterHeader.setText(QCoreApplication.translate("dialogLogin", u"Registracija", None))
        self.labelRegisterUsername.setText(QCoreApplication.translate("dialogLogin", u"Naujas vartotojas:", None))
        self.labelRegisterPassword.setText(QCoreApplication.translate("dialogLogin", u"Naujas slapta\u017eodis:", None))
        self.labelConfirmPassword.setText(QCoreApplication.translate("dialogLogin", u"Pakartokite slapta\u017eod\u012f:", None))
        self.buttonRegister.setText(QCoreApplication.translate("dialogLogin", u"Registruotis", None))
    # retranslateUi

