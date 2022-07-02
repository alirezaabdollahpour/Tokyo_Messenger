# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/g/onlinelessons/AP/project_messenger/interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chat_window(object):
    def setupUi(self, chat_window):
        chat_window.setObjectName("chat_window")
        chat_window.resize(953, 648)
        chat_window.setStyleSheet("QMainWindow {\n"
"        background-image: url(\"resourses/background.jpg\"); \n"
"        background-repeat: no-repeat; \n"
"        background-position: center;\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(chat_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_box = QtWidgets.QLineEdit(self.centralwidget)
        self.search_box.setStyleSheet("alternate-background-color: rgb(0, 255, 255);\n"
"background-color: rgb(189, 167, 255);\n"
"border: 2px solid blue;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.search_box.setObjectName("search_box")
        self.verticalLayout.addWidget(self.search_box)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sender_chat = QtWidgets.QListWidget(self.centralwidget)
        self.sender_chat.setStyleSheet("\n"
"QListView{\n"
"    border: 2px solid blue;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background-color: rgb(255, 170, 255)\n"
"}\n"
"QListView::item{\n"
"    border: 1px solid #6a6ea9;\n"
"}")
        self.sender_chat.setIconSize(QtCore.QSize(2, 2))
        self.sender_chat.setTextElideMode(QtCore.Qt.ElideNone)
        self.sender_chat.setObjectName("sender_chat")
        self.horizontalLayout_2.addWidget(self.sender_chat)
        self.resciver_chat = QtWidgets.QListWidget(self.centralwidget)
        self.resciver_chat.setStyleSheet("\n"
"QListView{\n"
"    border: 2px solid blue;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background-color: rgb(255, 170, 255)\n"
"}\n"
"QListView::item{\n"
"    border: 1px solid #6a6ea9;\n"
"}")
        self.resciver_chat.setAlternatingRowColors(False)
        self.resciver_chat.setWordWrap(False)
        self.resciver_chat.setObjectName("resciver_chat")
        self.horizontalLayout_2.addWidget(self.resciver_chat)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messege_box = QtWidgets.QLineEdit(self.centralwidget)
        self.messege_box.setStyleSheet("alternate-background-color: rgb(0, 255, 255);\n"
"background-color: rgb(189, 167, 255);\n"
"border: 2px solid blue;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.messege_box.setObjectName("messege_box")
        self.horizontalLayout.addWidget(self.messege_box)
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(0, 0, 255);\n"
"    border-radius: 6px;\n"
"    \n"
"    background-color: rgb(85, 85, 255);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.send_button.setObjectName("send_button")
        self.horizontalLayout.addWidget(self.send_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.contact_layout = QtWidgets.QVBoxLayout()
        self.contact_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.contact_layout.setContentsMargins(250, -1, -1, -1)
        self.contact_layout.setSpacing(7)
        self.contact_layout.setObjectName("contact_layout")
        self.gridLayout.addLayout(self.contact_layout, 0, 0, 1, 1)
        chat_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chat_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 953, 20))
        self.menubar.setObjectName("menubar")
        chat_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(chat_window)
        self.statusbar.setObjectName("statusbar")
        chat_window.setStatusBar(self.statusbar)

        self.retranslateUi(chat_window)
        QtCore.QMetaObject.connectSlotsByName(chat_window)

    def retranslateUi(self, chat_window):
        _translate = QtCore.QCoreApplication.translate
        chat_window.setWindowTitle(_translate("chat_window", "MainWindow"))
        self.search_box.setPlaceholderText(_translate("chat_window", "search"))
        self.messege_box.setPlaceholderText(_translate("chat_window", "type..."))
        self.send_button.setText(_translate("chat_window", "send"))
