# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lesson_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_LessonDialog(object):
    def setupUi(self, LessonDialog):
        if not LessonDialog.objectName():
            LessonDialog.setObjectName(u"LessonDialog")
        LessonDialog.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(LessonDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(LessonDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.subjectEdit = QLineEdit(self.widget)
        self.subjectEdit.setObjectName(u"subjectEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.subjectEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.typeEdit = QLineEdit(self.widget)
        self.typeEdit.setObjectName(u"typeEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.typeEdit)

        self.roomEdit = QLineEdit(self.widget)
        self.roomEdit.setObjectName(u"roomEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.roomEdit)

        self.teacherEdit = QLineEdit(self.widget)
        self.teacherEdit.setObjectName(u"teacherEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.teacherEdit)

        self.notesEdit = QTextEdit(self.widget)
        self.notesEdit.setObjectName(u"notesEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.notesEdit)

        self.examCheckBox = QCheckBox(self.widget)
        self.examCheckBox.setObjectName(u"examCheckBox")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.examCheckBox)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(LessonDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonOk = QPushButton(self.widget_2)
        self.buttonOk.setObjectName(u"buttonOk")

        self.horizontalLayout.addWidget(self.buttonOk)

        self.buttonCancel = QPushButton(self.widget_2)
        self.buttonCancel.setObjectName(u"buttonCancel")

        self.horizontalLayout.addWidget(self.buttonCancel)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.retranslateUi(LessonDialog)

        QMetaObject.connectSlotsByName(LessonDialog)
    # setupUi

    def retranslateUi(self, LessonDialog):
        LessonDialog.setWindowTitle(QCoreApplication.translate("LessonDialog", u"Paskaitos redagavimas", None))
        self.label.setText(QCoreApplication.translate("LessonDialog", u"Dalykas:", None))
        self.label_2.setText(QCoreApplication.translate("LessonDialog", u"Tipas:", None))
        self.label_3.setText(QCoreApplication.translate("LessonDialog", u"Auditorija:", None))
        self.label_4.setText(QCoreApplication.translate("LessonDialog", u"D\u0117stytojas:", None))
        self.label_5.setText(QCoreApplication.translate("LessonDialog", u"Pastabos:", None))
        self.label_6.setText(QCoreApplication.translate("LessonDialog", u"\u012eskaita / egzaminas:", None))
        self.examCheckBox.setText(QCoreApplication.translate("LessonDialog", u"Taip", None))
        self.buttonOk.setText(QCoreApplication.translate("LessonDialog", u"I\u0161saugoti", None))
        self.buttonCancel.setText(QCoreApplication.translate("LessonDialog", u"At\u0161aukti", None))
    # retranslateUi

