from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class TelegramUser(models.Model):
    username = models.CharField(max_length=100)
    telegram_id = models.BigIntegerField(unique=True)
