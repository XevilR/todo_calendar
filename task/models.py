from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)  # заголовок задачи
    description = models.TextField(blank=True)  # описание (необязательное)
    due_date = models.DateField(null=True, blank=True)  # дедлайн
    completed = models.BooleanField(default=False)  # выполнена или нет
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # кому принадлежит

    def __str__(self):
        return self.title