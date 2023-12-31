from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# создаем модель сообщения
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=100, blank=False)
    body = models.CharField(max_length=8000, blank=True)
    post_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'"{self.header}", автор: {self.author.username.title()}'

