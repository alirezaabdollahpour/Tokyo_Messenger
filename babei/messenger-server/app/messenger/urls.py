from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from web.views import (
    signup,
    signin,
    create_chat,
    get_chats,
    get_messages,
    send_message,
)

urlpatterns = [
    path("signup/", signup),
    path("signin/", signin),
    path("create_chat/", create_chat),
    path("get_chats/", get_chats),
    path("get_messages/", get_messages),
    path("send_message/", send_message),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
