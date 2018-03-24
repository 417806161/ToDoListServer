from django.core.validators import EmailValidator
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.BigIntegerField
    user_nickname = models.CharField(max_length=254)
    user_email = models.EmailField(max_length=254, validators=[EmailValidator])
    user_pwd = models.CharField(max_length=254)
    wechat_openid = models.CharField(max_length=254)
    wechat_union = models.CharField(max_length=254)
    user_headimg = models.CharField(max_length=254)
    user_id = models.CharField(max_length=254)


class Remind(models.Model):
    id = models.BigIntegerField
    user_id = models.CharField(max_length=254)
    task_id = models.CharField(max_length=254)
    remind_time = models.DateTimeField(auto_now=True)
    remind_type = models.CharField(max_length=1)
    isreminded = models.NullBooleanField()
    isdeal = models.NullBooleanField()
    remind_content = models.CharField(max_length=254)


class Task(models.Model):
    id = models.BigIntegerField
    task_id = models.CharField(max_length=254)
    task_title = models.CharField(max_length=254)
    task_parentid = models.CharField(max_length=254)
    user_id = models.CharField(max_length=254)
    remind_time = models.DateTimeField(auto_now=True)
    task_isremind = models.NullBooleanField()
    task_iscomplete = models.NullBooleanField()
    task_completetime = models.DateTimeField(auto_now=True)
