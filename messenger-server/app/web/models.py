from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"username:{self.username}"

class Chat(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")

    def __str__(self) -> str:
        return f"user1:{self.user1}-user2:{self.user2}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"chat:{self.chat}-user:{self.user}-text:{self.text[:50]}"
