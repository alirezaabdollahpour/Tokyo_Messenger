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


# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger('root')



def singup(username, password):
    # curl -X POST http://localhost:8000/signup/ -H 'Content-Type: application/json' -d '{"username":"jakeshkhan","password":"password"}'
    # singup with above curl command
    # define url
    url = "http://localhost:8000/signup/"
    # define headers
    headers = {'Content-Type': 'application/json'}
    # define data
    data = {'username': username, 'password': password}
    # send request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # return response
    return response

# response = singup("kianbehzad", "password")
# print(response.text)

# define singin function with this curl command :
# curl -X GET http://localhost:8000/signin/ -H 'Content-Type: application/json' -d '{"username":"jakeshkhan","password":"password"}'
def singin(username, password):
    # define url
    url = "http://localhost:8000/signin/"
    # define headers
    headers = {'Content-Type': 'application/json'}
    # define data
    data = {'username': username, 'password': password}
    # send request
    response = requests.get(url, headers=headers, data=json.dumps(data))
    # return response
    return response

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

# define get_chat_messages function with this curl command :
# curl -X GET http://localhost:8000/get_messages/ -H 'Content-Type: application/json' -d '{"token":"WJW1QTVZLGBKVMB2M8QQA2H1VCN9SAMLTLQQ23RJWV54I8XSMLZGGYTUJI7LF9X8L4ZSBR62GZHVA5MUO5946", "chat_id": 1}'
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

# define send_message function with this curl command :
# curl -X POST http://localhost:8000/send_message/ -H 'Content-Type: application/json' -d '{"token":"WJW1QTVZLGBKVMB2M8QQA2H1VCN9SAMLTLQQ23RJWV54I8XSMLZGGYTUJI7LF9X8L4ZSBR62GZHVA5MUO5946", "chat_id": 1, "text": "salam salar"}'
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


