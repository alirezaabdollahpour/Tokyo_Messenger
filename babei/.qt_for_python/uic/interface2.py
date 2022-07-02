# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/g/onlinelessons/AP/project_messenger/interface2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chat_window(object):
    def setupUi(self, chat_window):
        chat_window.setObjectName("chat_window")
        chat_window.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chat_window.sizePolicy().hasHeightForWidth())
        chat_window.setSizePolicy(sizePolicy)
        chat_window.setStyleSheet("background-image: url(\"resourses/background.jpg\"); \n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.centralwidget = QtWidgets.QWidget(chat_window)
        self.centralwidget.setObjectName("centralwidget")
        self.chat_box = QtWidgets.QWidget(self.centralwidget)
        self.chat_box.setGeometry(QtCore.QRect(230, 40, 571, 461))
        self.chat_box.setToolTip("")
        self.chat_box.setObjectName("chat_box")
        self.reciever_chat = QtWidgets.QListWidget(self.chat_box)
        self.reciever_chat.setEnabled(False)
        self.reciever_chat.setGeometry(QtCore.QRect(20, 0, 271, 461))
        self.reciever_chat.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.reciever_chat.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.reciever_chat.setAlternatingRowColors(False)
        self.reciever_chat.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.reciever_chat.setObjectName("reciever_chat")
        self.sender_chat = QtWidgets.QListWidget(self.chat_box)
        self.sender_chat.setEnabled(False)
        self.sender_chat.setGeometry(QtCore.QRect(290, 0, 271, 461))
        self.sender_chat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sender_chat.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sender_chat.setObjectName("sender_chat")
        self.message_box = QtWidgets.QLineEdit(self.centralwidget)
        self.message_box.setGeometry(QtCore.QRect(250, 510, 451, 41))
        self.message_box.setAcceptDrops(False)
        self.message_box.setObjectName("message_box")
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(710, 510, 80, 41))
        self.send_button.setObjectName("send_button")
        self.search_box = QtWidgets.QLineEdit(self.centralwidget)
        self.search_box.setGeometry(QtCore.QRect(250, 0, 541, 31))
        self.search_box.setAcceptDrops(True)
        self.search_box.setToolTip("")
        self.search_box.setToolTipDuration(5)
        self.search_box.setInputMask("")
        self.search_box.setText("")
        self.search_box.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.search_box.setObjectName("search_box")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.contact_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.contact_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.contact_layout.setContentsMargins(0, 0, 0, 0)
        self.contact_layout.setSpacing(1)
        self.contact_layout.setObjectName("contact_layout")
        chat_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chat_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        chat_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(chat_window)
        self.statusbar.setObjectName("statusbar")
        chat_window.setStatusBar(self.statusbar)

        self.retranslateUi(chat_window)
        self.reciever_chat.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(chat_window)

    def retranslateUi(self, chat_window):
        _translate = QtCore.QCoreApplication.translate
        chat_window.setWindowTitle(_translate("chat_window", "MainWindow"))
        self.message_box.setPlaceholderText(_translate("chat_window", "type..."))
        self.send_button.setText(_translate("chat_window", "send"))
        self.search_box.setPlaceholderText(_translate("chat_window", "search"))
