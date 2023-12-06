# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogWindow.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QSizePolicy, QWidget)

class Ui_ErrorQdialog(object):
    def setupUi(self, ErrorQdialog):
        if not ErrorQdialog.objectName():
            ErrorQdialog.setObjectName(u"ErrorQdialog")
        ErrorQdialog.resize(190, 64)
        self.gridLayout = QGridLayout(ErrorQdialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(ErrorQdialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ErrorQdialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ErrorQdialog)
        self.buttonBox.accepted.connect(ErrorQdialog.accept)
        self.buttonBox.rejected.connect(ErrorQdialog.reject)

        QMetaObject.connectSlotsByName(ErrorQdialog)
    # setupUi

    def retranslateUi(self, ErrorQdialog):
        ErrorQdialog.setWindowTitle(QCoreApplication.translate("ErrorQdialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ErrorQdialog", u"algum dos passos est\u00e1 incorreto!", None))
    # retranslateUi

