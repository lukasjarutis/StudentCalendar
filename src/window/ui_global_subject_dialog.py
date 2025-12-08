# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'global_subject_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_GlobalSubjectDialog(object):
    def setupUi(self, GlobalSubjectDialog):
        if not GlobalSubjectDialog.objectName():
            GlobalSubjectDialog.setObjectName(u"GlobalSubjectDialog")
        GlobalSubjectDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(GlobalSubjectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(GlobalSubjectDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.subjectEdit = QLineEdit(self.widget_2)
        self.subjectEdit.setObjectName(u"subjectEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.subjectEdit)

        self.typeEdit = QLineEdit(self.widget_2)
        self.typeEdit.setObjectName(u"typeEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.typeEdit)

        self.roomEdit = QLineEdit(self.widget_2)
        self.roomEdit.setObjectName(u"roomEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.roomEdit)

        self.teacherEdit = QLineEdit(self.widget_2)
        self.teacherEdit.setObjectName(u"teacherEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.teacherEdit)

        self.notesEdit = QLineEdit(self.widget_2)
        self.notesEdit.setObjectName(u"notesEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.notesEdit)

        self.examCheckBox = QCheckBox(self.widget_2)
        self.examCheckBox.setObjectName(u"examCheckBox")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.examCheckBox)

        self.repeatCombo = QComboBox(self.widget_2)
        self.repeatCombo.setObjectName(u"repeatCombo")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.repeatCombo)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.widget_2)

        self.groupBoxSchedule = QGroupBox(GlobalSubjectDialog)
        self.groupBoxSchedule.setObjectName(u"groupBoxSchedule")
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxSchedule)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayoutLessons = QGridLayout()
        self.gridLayoutLessons.setObjectName(u"gridLayoutLessons")

        self.verticalLayout_3.addLayout(self.gridLayoutLessons)


        self.verticalLayout.addWidget(self.groupBoxSchedule)

        self.widget = QWidget(GlobalSubjectDialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonOk = QPushButton(self.widget)
        self.buttonOk.setObjectName(u"buttonOk")

        self.horizontalLayout.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(self.widget)
        self.buttonCancel.setObjectName(u"buttonCancel")

        self.horizontalLayout.addWidget(self.buttonCancel)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(GlobalSubjectDialog)

        QMetaObject.connectSlotsByName(GlobalSubjectDialog)
    # setupUi

    def retranslateUi(self, GlobalSubjectDialog):
        GlobalSubjectDialog.setWindowTitle(QCoreApplication.translate("GlobalSubjectDialog", u"Naujas dalykas", None))
        self.label.setText(QCoreApplication.translate("GlobalSubjectDialog", u"\u012eskaita / egzaminas:", None))
        self.label_2.setText(QCoreApplication.translate("GlobalSubjectDialog", u"D\u0117stytojas:", None))
        self.label_3.setText(QCoreApplication.translate("GlobalSubjectDialog", u"Auditorija:", None))
        self.label_4.setText(QCoreApplication.translate("GlobalSubjectDialog", u"Tipas:", None))
        self.label_5.setText(QCoreApplication.translate("GlobalSubjectDialog", u"Dalykas:", None))
        self.label_6.setText(QCoreApplication.translate("GlobalSubjectDialog", u"Pastabos:", None))
        self.label_7.setText(QCoreApplication.translate("GlobalSubjectDialog", u"Pasikartojimas:", None))
        self.examCheckBox.setText(QCoreApplication.translate("GlobalSubjectDialog", u"Taip", None))
        self.groupBoxSchedule.setTitle(QCoreApplication.translate("GlobalSubjectDialog", u"Kada vyksta paskaitos?", None))
        self.buttonOk.setText(QCoreApplication.translate("GlobalSubjectDialog", u"Prid\u0117ti", None))
        self.buttonCancel.setText(QCoreApplication.translate("GlobalSubjectDialog", u"At\u0161aukti", None))
    # retranslateUi

