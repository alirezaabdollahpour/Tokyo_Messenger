# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/g/onlinelessons/AP/project_messenger/interface1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messenger_sign_window(object):
    def setupUi(self, messenger_sign_window):
        messenger_sign_window.setObjectName("messenger_sign_window")
        messenger_sign_window.resize(1005, 789)
        messenger_sign_window.setStyleSheet("QMainWindow {\n"
"        background-image: url(\"resourses/background.jpg\"); \n"
"        background-repeat: no-repeat; \n"
"        background-position: center;\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(messenger_sign_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.sign_up_username = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.sign_up_username.setFont(font)
        self.sign_up_username.setStyleSheet("alternate-background-color: rgb(0, 255, 255);\n"
"background-color: rgb(165, 255, 249);\n"
"border: 2px solid blue;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.sign_up_username.setInputMask("")
        self.sign_up_username.setText("")
        self.sign_up_username.setFrame(True)
        self.sign_up_username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.sign_up_username.setObjectName("sign_up_username")
        self.verticalLayout_2.addWidget(self.sign_up_username)
        self.sign_up_password = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sign_up_password.setFont(font)
        self.sign_up_password.setStyleSheet("alternate-background-color: rgb(0, 255, 255);\n"
"background-color: rgb(165, 255, 249);\n"
"border: 2px solid blue;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"")
        self.sign_up_password.setInputMask("")
        self.sign_up_password.setText("")
        self.sign_up_password.setFrame(True)
        self.sign_up_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sign_up_password.setObjectName("sign_up_password")
        self.verticalLayout_2.addWidget(self.sign_up_password)
        self.sign_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up_button.setSizeIncrement(QtCore.QSize(2, 2))
        self.sign_up_button.setBaseSize(QtCore.QSize(2, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sign_up_button.setFont(font)
        self.sign_up_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #0055ff;\n"
"    border-radius: 6px;\n"
"    \n"
"    background-color: rgb(170, 0, 255);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(24, 163, 255);\n"
"}\n"
"")
        self.sign_up_button.setObjectName("sign_up_button")
        self.verticalLayout_2.addWidget(self.sign_up_button)
        self.sign_up_status_box = QtWidgets.QLineEdit(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.sign_up_status_box.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.sign_up_status_box.setFont(font)
        self.sign_up_status_box.setStyleSheet("alternate-background-color: rgb(0, 255, 255);\n"
"background-color: rgb(165, 255, 249);\n"
"border: 2px solid blue;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.sign_up_status_box.setObjectName("sign_up_status_box")
        self.verticalLayout_2.addWidget(self.sign_up_status_box)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.sign_in_username = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setItalic(True)
        self.sign_in_username.setFont(font)
        self.sign_in_username.setStyleSheet("valternate-background-color: rgb(0, 255, 255);\n"
"background-color: rgb(165, 255, 249);\n"
"border: 2px solid blue;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.sign_in_username.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sign_in_username.setText("")
        self.sign_in_username.setObjectName("sign_in_username")
        self.verticalLayout.addWidget(self.sign_in_username)
        self.sign_in_password = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sign_in_password.setFont(font)
        self.sign_in_password.setStyleSheet("alternate-background-color: rgb(0, 255, 255);\n"
"background-color: rgb(165, 255, 249);\n"
"border: 2px solid blue;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.sign_in_password.setText("")
        self.sign_in_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sign_in_password.setObjectName("sign_in_password")
        self.verticalLayout.addWidget(self.sign_in_password)
        self.sign_in_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sign_in_button.setFont(font)
        self.sign_in_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #0055ff;\n"
"    border-radius: 6px;\n"
"    \n"
"    background-color: rgb(170, 0, 255);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(24, 163, 255);\n"
"}\n"
"")
        self.sign_in_button.setFlat(False)
        self.sign_in_button.setObjectName("sign_in_button")
        self.verticalLayout.addWidget(self.sign_in_button)
        self.sign_in_status_box = QtWidgets.QLineEdit(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 255, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.sign_in_status_box.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.sign_in_status_box.setFont(font)
        self.sign_in_status_box.setStyleSheet("alternate-background-color: rgb(0, 255, 255);\n"
"background-color: rgb(165, 255, 249);\n"
"border: 2px solid blue;\n"
"border-radius: 10px;\n"
"padding: 0 8px;")
        self.sign_in_status_box.setReadOnly(True)
        self.sign_in_status_box.setObjectName("sign_in_status_box")
        self.verticalLayout.addWidget(self.sign_in_status_box)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        messenger_sign_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(messenger_sign_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 20))
        self.menubar.setObjectName("menubar")
        messenger_sign_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(messenger_sign_window)
        self.statusbar.setObjectName("statusbar")
        messenger_sign_window.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(messenger_sign_window)
        self.toolBar.setObjectName("toolBar")
        messenger_sign_window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(messenger_sign_window)
        QtCore.QMetaObject.connectSlotsByName(messenger_sign_window)

    def retranslateUi(self, messenger_sign_window):
        _translate = QtCore.QCoreApplication.translate
        messenger_sign_window.setWindowTitle(_translate("messenger_sign_window", "MainWindow"))
        self.sign_up_username.setPlaceholderText(_translate("messenger_sign_window", "username"))
        self.sign_up_password.setPlaceholderText(_translate("messenger_sign_window", "password"))
        self.sign_up_button.setText(_translate("messenger_sign_window", "Sign up"))
        self.sign_in_username.setPlaceholderText(_translate("messenger_sign_window", "username"))
        self.sign_in_password.setPlaceholderText(_translate("messenger_sign_window", "password"))
        self.sign_in_button.setText(_translate("messenger_sign_window", "Sign in"))
        self.toolBar.setWindowTitle(_translate("messenger_sign_window", "toolBar"))
