# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_card.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Game_Card(QWidget):
    def __init__(self, game_data):
        super(Game_Card, self).__init__()
        self.setupUi(self, game_data)

    def setupUi(self, Form, game_data):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setFixedSize(180, 240)
        self.game_data = game_data
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gameName = QLabel(self.frame)
        self.gameName.setObjectName(u"gameName")

        self.verticalLayout_2.addWidget(self.gameName)

        self.gameImage = QLabel(self.frame)
        self.gameImage.setObjectName(u"gameImage")

        self.verticalLayout_2.addWidget(self.gameImage)

        self.btnPlay = QPushButton(self.frame)
        self.btnPlay.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPlay.setObjectName(u"btnPlay")
        

        self.verticalLayout_2.addWidget(self.btnPlay)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gameName.setText(QCoreApplication.translate("Form", self.game_data["name"], None))
        self.gameImage.setText(QCoreApplication.translate("Form", self.game_data["category"], None))
        self.btnPlay.setText(QCoreApplication.translate("Form", u"Play", None))
    # retranslateUi

