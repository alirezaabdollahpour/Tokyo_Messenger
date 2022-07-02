from http import client
import os
import numpy as np
import os
import sys
import threading
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as figure_canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as navigation_toolbar
from matplotlib.figure import Figure
from PyQt5 import uic, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow , QVBoxLayout, QWidget, QPushButton, QSizePolicy,QGridLayout,QListWidget,QListWidgetItem
from urllib import response
import requests
import json
import os
import sys
from messenger_client.client import client
from time import sleep

#setting qt forms 
form = uic.loadUiType(os.path.join(os.getcwd() , "interface1.ui"))[0]
form2 = uic.loadUiType(os.path.join(os.getcwd() , "interface_chat.ui"))[0]

class messenger_sign_window(QMainWindow, form):
    def __init__(self, client1, w2) -> None:
        super(messenger_sign_window, self).__init__()
        self.setupUi(self)
        
        # connecting buttons
        self.sign_up_button.clicked.connect(self.sign_up)
        self.sign_in_button.clicked.connect(self.sign_in)
        self.sign_up_status_box.hide()
        self.sign_in_status_box.hide()
        self.token = ""

    def sign_up(self):
        username = self.sign_up_username.text()
        password = self.sign_up_password.text()
        
        #check username and password
        if(username =="" or password == ""):
            self.sign_up_status_box.show()
            self.sign_up_status_box.setText("please enter username or password")
            return
        
        # requesting to server
        url = "http://localhost:8000/signup/"
        # define headers
        headers = {'Content-Type': 'application/json'}
        # define data
        data = {'username': username, 'password': password}
        # send request
        response = requests.post(url, headers=headers, data=json.dumps(data))
        # return response
        self.sign_up_status_box.show()
        
        if(("\"status\": \"ok\"") in response.text):
            self.sign_up_status_box.setText("you signed up successfully")
            self.sign_up_username.setText("")
            self.sign_up_password.setText("")
        elif((response.text).find("\"status\": \"Error\"")):
            self.sign_up_status_box.setText(response.text[12 : len(response.text) - 2])
            
        return response
    
    def sign_in(self):
        username = self.sign_in_username.text()
        password = self.sign_in_password.text()
        
        #check username and password
        if(username =="" or password == ""):
            self.sign_in_status_box.show()
            self.sign_in_status_box.setText("enter username or password")
            return
        