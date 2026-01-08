# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget, QDialog)
from game_card import *
from add_form import Add_Dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self) 
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(957, 576)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #0f1a2b;  /* azul muy oscuro */\n"
"    color: #f8c0f0;             /* rosa claro para texto general */\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 12pt;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.menu_2 = QFrame(self.centralwidget)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setStyleSheet(u"QFrame {\n"
"    background-color: #11203b;   /* azul oscuro */\n"
"    border-bottom: 2px solid #1a2a4b;\n"
"}\n"
"\n"
"/* Botones del men\u00fa */\n"
"QPushButton {\n"
"    background-color: #1a2a4b;   /* azul oscuro */\n"
"    color: #f8c0f0;              /* rosa claro */\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2e3a6b;   /* azul medio para hover */\n"
"    color: #ff99ff;              /* rosa m\u00e1s brillante al pasar */\n"
"}\n"
"\n"
"/* QLineEdit de b\u00fasqueda */\n"
"QLineEdit{\n"
"    background-color: #1a2a4b;\n"
"    color: #f8c0f0;\n"
"    border: 1px solid #2e3a6b;\n"
"    border-radius: 5px;\n"
"    padding: 4px 8px;\n"
"}")
        self.menu = QHBoxLayout(self.menu_2)
        self.menu.setObjectName(u"menu")
        self.label = QLabel(self.menu_2)
        self.label.setObjectName(u"label")

        self.menu.addWidget(self.label)

        self.lineEdit = QLineEdit(self.menu_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.menu.addWidget(self.lineEdit)

        self.btnTodos = QPushButton(self.menu_2)
        self.btnTodos.setObjectName(u"btnTodos")

        self.menu.addWidget(self.btnTodos)

        self.btnCategorias = QPushButton(self.menu_2)
        self.btnCategorias.setObjectName(u"btnCategorias")

        self.menu.addWidget(self.btnCategorias)

        self.btnConfiguracion = QPushButton(self.menu_2)
        self.btnConfiguracion.setObjectName(u"btnConfiguracion")

        self.menu.addWidget(self.btnConfiguracion)


        self.verticalLayout_2.addWidget(self.menu_2)

        self.gamesScroll = QScrollArea(self.centralwidget)
        self.gamesScroll.setObjectName(u"gamesScroll")
        self.gamesScroll.setStyleSheet(u"/* ScrollArea / zona de juegos */\n"
"#gamesScroll {\n"
"    background-color: #0f1a2b;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Contenedor de tarjetas */\n"
"#gamesContainer {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Tarjeta de juego (GameCard) */\n"
"#gameCard {\n"
"    background-color: #11203b;   /* azul oscuro */\n"
"    border: 1px solid #1a2a4b;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"#gameTitle {\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    color: #f8c0f0;\n"
"}\n"
"\n"
"#gameCategory {\n"
"    font-size: 10pt;\n"
"    color: #ff99ff;  /* rosa */\n"
"}\n"
"\n"
"#btnPlay {\n"
"    background-color: #1a2a4b;\n"
"    color: #f8c0f0;\n"
"    border: none;\n"
"    padding: 6px 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#btnPlay:hover {\n"
"    background-color: #2e3a6b;\n"
"    color: #ff99ff;\n"
"}")
        self.gamesScroll.setWidgetResizable(True)
        self.gamesContainer = QWidget()
        self.gamesContainer.setObjectName(u"gamesContainer")
        self.gamesContainer.setGeometry(QRect(0, 0, 937, 456))
        self.gamesContainer.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.gamesContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnAdd = QPushButton(self.gamesContainer)
        self.btnAdd.setFixedSize(180, 220)
        self.btnAdd.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAdd.clicked.connect(self.open_add_dialog)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setStyleSheet(u"#btnAdd {\n"
"    background-color: rgba(100, 100, 100, 0.6); /* gris difuminado semi-transparente */\n"
"    color: white;               /* texto blanco */\n"
"    border-radius: 12px;        /* bordes redondeados */\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btnAdd:hover {\n"
"    background-color: rgba(120, 120, 120, 0.8); /* gris m\u00e1s claro al hover */\n"
"}")

        self.gridLayout.addWidget(self.btnAdd, 0, 0, 1, 1)

        self.gamesScroll.setWidget(self.gamesContainer)

        self.verticalLayout_2.addWidget(self.gamesScroll)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 957, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        game_example = {
            "name": "Super Test Game",
            "category": "Acción",
            "exe": "C:/Juegos/SuperTestGame/game.exe",
            "image": "C:/Users/david/Desktop/DESMUME - 64 bits/a.png"
        }

        # Suponiendo que GameCard toma un diccionario con los datos del juego
        card = Game_Card(game_example)

        """col_count = 4  # nº de tarjetas por fila

        row = index // col_count
        col = index % col_count"""
        
        row = 0
        col = 1

        self.gridLayout.addWidget(card, row, col)

        
        self.gridLayout.setSpacing(10)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)

        self.gridLayout.addWidget(self.btnAdd, 0, 0)
        self.gridLayout.addWidget(card, 0, 1)

        self.gridLayout.setColumnStretch(0, 0)
        self.gridLayout.setColumnStretch(1, 0)
        self.gridLayout.setColumnStretch(2, 1)



        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Game Launcher", None))
        self.btnTodos.setText(QCoreApplication.translate("MainWindow", u"Todos los juegos", None))
        self.btnCategorias.setText(QCoreApplication.translate("MainWindow", u"Categor\u00edas", None))
        self.btnConfiguracion.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"+ Add Game", None))
    # retranslateUi

    def open_add_dialog(self):
        self.add_game_dialog = Add_Game_Dialog()
        self.add_game_dialog.show()

class Add_Game_Dialog(Add_Dialog, QDialog):
    def __init__(self):
        super(Add_Game_Dialog, self).__init__()
        self.setupUi(self)