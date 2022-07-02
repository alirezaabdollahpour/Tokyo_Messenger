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