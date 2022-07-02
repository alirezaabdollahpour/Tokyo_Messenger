# request to the django server for messenger
import requests
import json
import os
import sys
import time
import datetime
import threading
import queue
import random
import string
import logging
import logging.handlers
import logging.config
import asyncio
from urllib import response
import requests
import json
import os
import sys
import time

# define singin function with this curl command :
# curl -X GET http://localhost:8000/signin/ -H 'Content-Type: application/json' -d '{"username":"jakeshkhan","password":"password"}'

# define create_chat function with this curl command :
# curl -X POST http://localhost:8000/create_chat/ -H 'Content-Type: application/json' -d '{"token":"WJW1QTVZLGBKVMB2M8QQA2H1VCN9SAMLTLQQ23RJWV54I8XSMLZGGYTUJI7LF9X8L4ZSBR62GZHVA5MUO5946","user2name":"jakeshkhan2"}'
def create_chat(token, user2name):
    # define url
    url = "http://localhost:8000/create_chat/"
    # define headers
    headers = {'Content-Type': 'application/json'}
    # define data
    data = {'token': token, 'user2name': user2name}
    # send request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # return response
    return response

# define get_chat function with this curl command :
# curl -X GET http://localhost:8000/get_chats/ -H 'Content-Type: application/json' -d '{"token":"WJW1QTVZLGBKVMB2M8QQA2H1VCN9SAMLTLQQ23RJWV54I8XSMLZGGYTUJI7LF9X8L4ZSBR62GZHVA5MUO5946"}'
def get_chats(token):
    # define url
    url = "http://localhost:8000/get_chats/"
    # define headers
    headers = {'Content-Type': 'application/json'}
    # define data
    data = {'token': token}
    # send request
    response = requests.get(url, headers=headers, data=json.dumps(data))
    # return response
    return response

def get_messages(token, chat_id):
    # define url
    url = "http://localhost:8000/get_messages/"
    # define headers
    headers = {'Content-Type': 'application/json'}
    # define data
    data = {'token': token, 'chat_id': chat_id}
    # send request
    response = requests.get(url, headers=headers, data=json.dumps(data))
    # return response
    return response


def send_message(token, chat_id, text):
    # define url
    url = "http://localhost:8000/send_message/"
    # define headers
    headers = {'Content-Type': 'application/json'}
    # define data
    data = {'token': token, 'chat_id': chat_id, 'text': text}
    # send request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # return response
    return response

class client:
    # define constructor
    def __init__(self, username = "", token = ""):
        # define username
        self.username = username
        # define token
        self.token = token
        # define chats
        self.chats = dict({})
        
        self.reciever = ""
        # define messages
        self.messages = []
        # define chat_id
        self.chat_id = 0
        # define message_id
        self.message_id = 0
        # define message_text
        self.message_text = ""
        # define message_time
        self.message_time = ""
        # define message_sender


    # define above create_chat function in this class
    def create_chat(self, user2name):
        # call create_chat function
        response = create_chat(self.token, user2name)
        # return response
        return response

    # define above get_chats function in this class
    def get_chats(self):
        # call get_chats function
        response = get_chats(self.token)
        # return response
        return response

    # define above get_chat_messages function in this class
    def get_messages(self, chat_id):
        # call get_chat_messages function
        response = get_messages(self.token, chat_id)
        # return response
        return response

    # define above send_message function in this class
    def send_message(self, chat_id, text):
        # call send_message function
        response = send_message(self.token, chat_id, text)
        # return response
        return response

        