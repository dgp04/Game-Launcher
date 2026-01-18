# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget, QFileDialog)
import os
import configparser

class Add_Dialog(QDialog):
        
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 440)
        Dialog.setStyleSheet(u"QDialog {\n"
"    background-color: #1e1e2f; /* azul oscuro */\n"
"    color: #f48fb1;            /* rosa para textos */\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #f48fb1; \n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2c2c3c;\n"
"    border: 1px solid #f48fb1;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3a3a4d;\n"
"    color: #f48fb1;\n"
"    border: 1px solid #f48fb1;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #50506a;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 40)
        self.label_add = QLabel(Dialog)
        self.label_add.setObjectName(u"label_add")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_add.setFont(font)
        self.label_add.setStyleSheet(u"#label_add{\n"
"fontSize: 20p;\n"
"} ")

        self.verticalLayout.addWidget(self.label_add)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.gameForm = QFormLayout()
        self.gameForm.setObjectName(u"gameForm")
        self.gameForm.setHorizontalSpacing(12)
        self.gameForm.setVerticalSpacing(30)
        self.nameLabel = QLabel(Dialog)
        self.nameLabel.setObjectName(u"nameLabel")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.nameLabel.setFont(font1)

        self.gameForm.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(Dialog)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.gameForm.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.category_label = QLabel(Dialog)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setFont(font1)

        self.gameForm.setWidget(1, QFormLayout.LabelRole, self.category_label)

        self.categoryLineEdit = QLineEdit(Dialog)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")

        self.gameForm.setWidget(1, QFormLayout.FieldRole, self.categoryLineEdit)

        self.btnExe = QPushButton(Dialog)
        self.btnExe.setObjectName(u"btnExe")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.btnExe.setFont(font2)
        self.btnExe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnExe.clicked.connect(self.select_exe_path)

        self.gameForm.setWidget(2, QFormLayout.SpanningRole, self.btnExe)

        self.imageBtn = QPushButton(Dialog)
        self.imageBtn.setObjectName(u"imageBtn")
        self.imageBtn.setFont(font2)
        self.imageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.imageBtn.clicked.connect(self.select_image_path)

        self.gameForm.setWidget(3, QFormLayout.SpanningRole, self.imageBtn)


        self.verticalLayout_2.addLayout(self.gameForm)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 40)
        self.btnAddGame = QPushButton(Dialog)
        self.btnAddGame.setObjectName(u"btnAddGame")
        self.btnAddGame.setFont(font2)
        self.btnAddGame.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddGame.clicked.connect(self.add_game)

        self.horizontalLayout_2.addWidget(self.btnAddGame)

        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.clicked.connect(self.close)
        self.btnCancel.setFont(font2)
        self.btnCancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnCancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 30)
        self.verticalLayout_2.setStretch(2, 10)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Game", None))
        self.label_add.setText(QCoreApplication.translate("Dialog", u"Add Game", None))
        self.nameLabel.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.category_label.setText(QCoreApplication.translate("Dialog", u"Category:", None))
        self.btnExe.setText(QCoreApplication.translate("Dialog", u"Select game path...", None))
        self.imageBtn.setText(QCoreApplication.translate("Dialog", u"Select cover image path...", None))
        self.btnAddGame.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

    def select_exe_path(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select game executable",
            "",
            "Executable files (*.exe);;All files (*)"
        )

        if file_path:
            self.btnExe.setText(file_path)
            self.game_path = file_path 
            
    def select_image_path(self):
        image_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select game cover",
            "",
            "Executable files (*.jpg, *.png);;All files (*)"
        )

        if image_path:
            self.imageBtn.setText(image_path)
            self.cover_path = image_path 
    
    def save_game_to_ini(self, game_data):
        config = configparser.ConfigParser()
        GAMES_INI = "games.ini"

        # Si existe, lo cargamos
        if os.path.exists(GAMES_INI):
            config.read(GAMES_INI, encoding="utf-8")

        section = game_data["name"]

        if not config.has_section(section):
            config.add_section(section)

        config.set(section, "category", game_data["category"])
        config.set(section, "exe", game_data["exe"])
        config.set(section, "image", game_data["image"])
        print(game_data["image"])
        print(config.get(section, "image"))

        with open(GAMES_INI, "w", encoding="utf-8") as f:
            config.write(f)
            
    def add_game(self):
        name = self.nameLineEdit.text().strip()
        category = self.categoryLineEdit.text().strip()
        exe = getattr(self, "game_path", "")
        image = getattr(self, "cover_path", "")
        
        print("image: ", image)

        if not name or not exe:
            return

        game_data = {
            "name": name,
            "category": category,
            "exe": exe,
            "image": image
        }

        self.save_game_to_ini(game_data)  # ← AQUÍ
        self.accept()                     # ← DESPUÉS

