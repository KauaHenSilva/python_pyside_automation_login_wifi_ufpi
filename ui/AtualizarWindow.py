# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AtualizarWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(455, 166)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Atulizar Driver", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Ol\u00e1, Pelo visto voc\u00ea tem um drive desuatalizado.<br/>Siga esses passos para atualizar:</p><p>1. Conectar com alguma fonte de internet, 4G ou semelhante.</p><p>2. Ter o navegador Edge instalado.</p><p>3. Clicar no bot\u00e3o atualizar.</p><p>Obs: Descupa, Infelismente o seu aplicativo s\u00f3 vai funcionar caso esteja atualizado.</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Atualizar", None))
    # retranslateUi

