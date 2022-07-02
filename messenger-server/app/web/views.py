from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json
import random
import string

from .models import User, Chat, Message
from datetime import date, datetime

# Create your views here.

# JsonResponse({'foo':'bar'})
def get_random_str(N):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

def merge_chats(c1, c2):
    chats = []
    i, j = 0, 0
    while (i < len(c1)) or (j < len(c2)):
        if i == len(c1) and j == len(c2):
            break
        
        if i == len(c1):
            chats += [[c2[j].text, c2[j].user.username]]
            j += 1
            continue
        if j == len(c2):
            chats += [[c1[i].text, c1[i].user.username]]
            i += 1
            continue

        if c1[i].time < c2[j].time:
            chats += [[c1[i].text, c1[i].user.username]]
            i += 1
        else:
            chats += [[c2[j].text, c2[j].user.username]]
            j += 1
    return chats

@csrf_exempt
def signup(req: HttpRequest):
    if req.method == "POST":
        data = json.loads(req.body)
        if (not "username" in data) or (not "password" in data):
            return JsonResponse({"status": "Error. please enter username or password"})
        
        # TODO: validate that username and password field be at least 8 chars
        username = data["username"]
        password = data["password"]
        token = get_random_str(85)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "Error. this username is already exists"})

        user = User(username=username, password=password, token=token)
        user.save()

        return JsonResponse({"status": "ok", "user_id": str(user.id)})

    return JsonResponse({"status": "Error. you must use POST method"})
        

def signin(req: HttpRequest):
    if req.method == "GET":
        data = json.loads(req.body)

        if (not "username" in data) or (not "password" in data):
            return JsonResponse({"status":"Error. please enter username or password"})

        username = data["username"]
        password = data["password"]

        try:
            user = User.objects.filter(username=username, password=password).get()
            return JsonResponse({"status": "ok", "token": user.token})
        except:
            return JsonResponse({"status": "Error. usre is not exists"})

    return JsonResponse({"status": "Error. you must use Get method"})


@csrf_exempt
def create_chat(req: HttpRequest):
    if req.method == "POST":
        data = json.loads(req.body)
        if (not "token" in data) or (not "user2name" in data):
            return JsonResponse({"status": "Error. please enter token or user2name"})
        
        token = data["token"]
        user2name = data["user2name"]
        
        if  not Chat.objects.filter(user1__token=token, user2__username=user2name).exists():
            pass
        else:
            return JsonResponse({"status": "Chat_Error", "chat_id": str(Chat.objects.filter(user1__token=token, user2__username=user2name).get().id)})
        if  not Chat.objects.filter(user2__token=token, user1__username=user2name).exists():
            pass
        else: 
            return JsonResponse({"status": "Chat_Error", "chat_id": str(Chat.objects.filter(user2__token=token, user1__username=user2name).get().id)})
            

        if User.objects.filter(username=user2name).exists() and \
            User.objects.filter(token=token).exists() and \
            User.objects.filter(username=user2name).get() != \
            User.objects.filter(token=token).get():

            u1 = User.objects.filter(token=token).get()
            u2 = User.objects.filter(username=user2name).get()
            chat = Chat(user1=u1, user2=u2)
            chat.save()

            return JsonResponse({"status": "ok", "chat_id": str(chat.id)})

        return JsonResponse({"status": "Error"})

    return JsonResponse({"status": "Error. you must use POST method"})
    

def get_chats(req: HttpRequest):
    if req.method == "GET":
        data = json.loads(req.body)

        if not "token" in data:
            return JsonResponse({"status": "Error. please enter token"})

        token = data["token"]

        # ["chat_id", "user2"]
        chats = []
        qset = Chat.objects.filter(user1__token=token).all()
        for obj in qset:
            chats.append([obj.id, obj.user2.username])
        qset = Chat.objects.filter(user2__token=token).all()
        for obj in qset:
            chats.append([obj.id, obj.user1.username])
        return JsonResponse({"status": "ok", "chats": chats})

    return JsonResponse({"status": "Error. you must use GET method"})


def get_messages(req: HttpRequest):
    if req.method == "GET":
        data = json.loads(req.body)
        
        if (not "token" in data) or (not "chat_id" in data):
            return JsonResponse({"status": "Error. please enter token or username"})

        token = data["token"]
        chat_id = int(data["chat_id"])

        chat = Chat.objects.filter(id=chat_id).get()
        if not (chat.user1.token == token or chat.user2.token == token):
            return JsonResponse({"status": "Error. opss ypu are not allowed to see this chat"})
        
        u1_chats = Message.objects.filter(chat_id=chat_id, user=chat.user1).order_by("time").all()
        u2_chats = Message.objects.filter(chat_id=chat_id, user=chat.user2).order_by("time").all()
        chats = merge_chats(u1_chats, u2_chats)
        return JsonResponse({"status": "ok", "chats": chats})
        

    return JsonResponse({"status": "Error. you must use GET method"})


@csrf_exempt
def send_message(req: HttpRequest):
    if req.method == "POST":
        data = json.loads(req.body)
        if (not "token" in data) or (not "chat_id" in data) or (not "text" in data):
            return JsonResponse({"status": "Error. please enter token or chat_id or text"})
        
        token = data["token"]
        chat_id = int(data["chat_id"])
        text = data["text"]

        if Chat.objects.filter(id=chat_id, user1__token=token).exists() or \
            Chat.objects.filter(id=chat_id, user2__token=token).exists():
            user = User.objects.filter(token=token).get()
            chat = Chat.objects.filter(id=chat_id).get()
            msg = Message(chat=chat, user=user, text=text, time=datetime.now())
            msg.save()
            return JsonResponse({"status": "ok", "msg_id": str(msg.id)})

        return JsonResponse({"status": "Error"})

    return JsonResponse({"status": "Error. you must use Post method"})
