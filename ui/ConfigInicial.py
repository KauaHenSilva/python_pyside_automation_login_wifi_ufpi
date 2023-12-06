# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigInicial.ui'
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

class Ui_ConfigInicial(object):
    def setupUi(self, ConfigInicial):
        if not ConfigInicial.objectName():
            ConfigInicial.setObjectName(u"ConfigInicial")
        ConfigInicial.resize(386, 166)
        self.verticalLayout_2 = QVBoxLayout(ConfigInicial)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ConfigInicial)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.ButtonConfig = QPushButton(ConfigInicial)
        self.ButtonConfig.setObjectName(u"ButtonConfig")

        self.verticalLayout.addWidget(self.ButtonConfig)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ConfigInicial)

        QMetaObject.connectSlotsByName(ConfigInicial)
    # setupUi

    def retranslateUi(self, ConfigInicial):
        ConfigInicial.setWindowTitle(QCoreApplication.translate("ConfigInicial", u"Config Inicial", None))
        self.label.setText(QCoreApplication.translate("ConfigInicial", u"<html><head/><body><p>Ol\u00e1, Para utilizar esse aplicativo voc\u00ea tem que realizar esses requisitos:<br/>(Essa prossedimento s\u00f3 \u00e9 feito uma vez)</p><p>1. Conectar com alguma fonte de internet, 4G ou semelhante.</p><p>2. Ter o navegador Edge instalado.</p><p>3. Clicar no bot\u00e3o Configurar. :)</p></body></html>", None))
        self.ButtonConfig.setText(QCoreApplication.translate("ConfigInicial", u"Configurar", None))
    # retranslateUi

