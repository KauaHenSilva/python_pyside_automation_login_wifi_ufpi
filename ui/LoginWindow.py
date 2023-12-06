# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_WindowLogin(object):
    def setupUi(self, WindowLogin):
        if not WindowLogin.objectName():
            WindowLogin.setObjectName(u"WindowLogin")
        WindowLogin.resize(336, 121)
        WindowLogin.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(WindowLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lembrarMe = QCheckBox(self.centralwidget)
        self.lembrarMe.setObjectName(u"lembrarMe")
        self.lembrarMe.setFocusPolicy(Qt.ClickFocus)
        self.lembrarMe.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.lembrarMe.setChecked(True)

        self.gridLayout.addWidget(self.lembrarMe, 3, 1, 1, 1)

        self.passwordLabel = QLabel(self.centralwidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 2, 1, 1, 1)

        self.userLabel = QLabel(self.centralwidget)
        self.userLabel.setObjectName(u"userLabel")

        self.gridLayout.addWidget(self.userLabel, 0, 1, 1, 1)

        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setMinimumSize(QSize(100, 20))
        self.passwordLineEdit.setFocusPolicy(Qt.StrongFocus)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.passwordLineEdit, 2, 2, 1, 1)

        self.userLineEdit = QLineEdit(self.centralwidget)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setMinimumSize(QSize(100, 20))
        self.userLineEdit.setFocusPolicy(Qt.StrongFocus)
        self.userLineEdit.setEchoMode(QLineEdit.Normal)
        self.userLineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.userLineEdit.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.userLineEdit, 0, 2, 1, 1)

        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout.addWidget(self.loginButton, 3, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        WindowLogin.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.userLineEdit, self.passwordLineEdit)

        self.retranslateUi(WindowLogin)

        QMetaObject.connectSlotsByName(WindowLogin)
    # setupUi

    def retranslateUi(self, WindowLogin):
        WindowLogin.setWindowTitle(QCoreApplication.translate("WindowLogin", u"LoginUfpi", None))
#if QT_CONFIG(statustip)
        self.lembrarMe.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lembrarMe.setText(QCoreApplication.translate("WindowLogin", u"Salvar Login?", None))
        self.passwordLabel.setText(QCoreApplication.translate("WindowLogin", u"Senha:", None))
        self.userLabel.setText(QCoreApplication.translate("WindowLogin", u"Usuario:", None))
        self.passwordLineEdit.setInputMask("")
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("WindowLogin", u"Utilize a sua senha do Sigaa! :)", None))
        self.userLineEdit.setPlaceholderText(QCoreApplication.translate("WindowLogin", u"Utilize o seu usu\u00e1rio do Sigaa! :)", None))
        self.loginButton.setText(QCoreApplication.translate("WindowLogin", u"Login", None))
    # retranslateUi

