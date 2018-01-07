from django.db import models
from django.contrib import admin
from django.utils.html import format_html
# Create your models here.
class User(models.Model):
    gender = (('male','男'),('female','女'),)

    name = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    address = models.CharField(max_length=128)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-create_time"]   # -号代表降序
        verbose_name = "用户"
        verbose_name_plural = "用户"
