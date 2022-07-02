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
        
        #requesting to server
        url = "http://localhost:8000/signin/"
        # define headers
        headers = {'Content-Type': 'application/json'}
        # define data
        data = {'username': username, 'password': password}
        # send request
        response = requests.get(url, headers=headers, data=json.dumps(data))
        # return response
        
        #openning chat page
        if(("\"status\": \"ok\"") in response.text):
            client1.username = username
            client1.token = response.json()["token"]
            w2.show()
            
            
        elif((response.text).find("\"status\": \"Error\"")):
            self.sign_in_status_box.show()
            self.sign_in_status_box.setText("please check your username or password")
            
        return response

#chat page

class chat_window(QMainWindow, form2):
    def __init__(self, client1) -> None:
        super(chat_window, self).__init__()
        self.setupUi(self)
        self.Thread_list = []
        
        #connecting buttons
        self.search_box.returnPressed.connect(self.search)
        self.send_button.setDisabled(True)
        self.send_button.clicked.connect(self.send_message)
        
    #search for usernames and check if a chat exists or not
    def search(self):
        
        text = self.search_box.text()
        response = client1.create_chat(text)
        if(not(response.json()["status"] == "Chat_Error")):
            if(response.json()["status"] == "Error"):
                self.search_box.setText("user not found")
                return
            
            #adding contact
            else:
                new_contact = QPushButton(text)
                new_contact.setGeometry(0,0,231,61)
                new_contact.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
                new_contact.setMinimumSize(231,61)
                new_contact.setStyleSheet(stylesheet2)
                self.contact_layout.addWidget(new_contact)
                new_contact.clicked.connect(lambda: self.lets_chat(new_contact.text()))
                client1.chats[text] = response.json()["chat_id"]
                return
        #add contact with pre defined chat
        else:
            self.search_box.setText("chat already exists")
            client1.chats[text] = response.json()["chat_id"]
            new_contact = QPushButton(text)
            new_contact.setGeometry(0,0,231,61)
            new_contact.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
            new_contact.setMinimumSize(231,61)
            new_contact.setStyleSheet(stylesheet2)
            self.contact_layout.addWidget(new_contact)
            new_contact.clicked.connect(lambda: self.lets_chat(new_contact.text()))
        
    def send_message(self):
        # get message text
        text = self.message_box.text()
        # get chat id
        chat_id = client1.chats[client1.reciever]
        # send message
        response = client1.send_message(chat_id, text)
        # return response
        self.message_box.setText("")
    
    #showing chats uing refreshing via threads    
    def lets_chat(self, text):
        #check if any thread is running if yes shut it down
        if len(self.Thread_list) != 0:
            for th in self.Thread_list:
                th.terminate()
        client1.reciever = text
        self.send_button.setDisabled(False)
        self.Thread = Chat_Thread(self)
        self.Thread_list.append(self.Thread)
        self.Thread.update_trigger.connect(self.update)
        self.Thread.start()
        
    #update function that is cslled via thread for refreshing chat every 0.1 second
    def update(self):
        self.sender_chat.clear()
        self.reciever_chat.clear()
        chat_id = client1.chats[client1.reciever]
        messages = (client1.get_messages(chat_id)).json()["chats"]
        for pm in messages:
            #check if message is for signed in user
            if(pm[1] == client1.username):
                text_message = QListWidgetItem(pm[0] + ":" + client1.username)
                text_indent = QListWidgetItem("")
                self.sender_chat.addItem(text_indent)
                self.reciever_chat.addItem(text_message)
            elif(pm[1] == client1.reciever):
                text_message = QListWidgetItem(client1.reciever + ":" + pm[0])
                text_indent = QListWidgetItem("")
                self.reciever_chat.addItem(text_indent)
                self.sender_chat.addItem(text_message)

#thread class for refreshing message page

class Chat_Thread(QtCore.QThread):
    update_trigger = QtCore.pyqtSignal()
    
    def __init__(self, window) -> None:
        QtCore.QThread.__init__(self, parent=window)
    def run(self):
        while(True):
            print(self.__str__)
            sleep(0.1)
            self.update_trigger.emit()


#background sheet
stylesheet = """
    messenger_sign_window {
        background-image: url("resourses/background2.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""
stylesheet2 = """
    QPushButton {
    border: 2px solid #0055ff;
    border-radius: 6px;
    font: italic 12pt "Sans Serif";
  background-color: rgb(170, 0, 255);
    min-width: 80px;
}

QPushButton:pressed {
  background-color: rgb(24, 163, 255);
}"""