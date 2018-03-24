from django.db import models

# Create your models here.


class User(models.Model):
    id = models.BigIntegerField
    user_nickname = models.CharField(max_length=225)
    user_email = models.EmailField
    user_pwd = models.CharField(max_length=225)
    wechat_openid = models.CharField(max_length=225)
    wechat_union = models.CharField(max_length=225)
    user_headimg = models.CharField(max_length=225)
    user_id = models.CharField(max_length=225)


class Remind(models.Model):
    id = models.BigIntegerField
    user_id = models.CharField(max_length=225)
    task_id = models.CharField(max_length=225)
    remind_time = models.DateTimeField
    remind_type = models.CharField(max_length=1)
    isreminded = models.BooleanField
    isdeal = models.BooleanField
    remind_content = models.CharField(max_length=225)


class Task(models.Model):
    id = models.BigIntegerField
    task_id = models.CharField(max_length=225)
    task_title = models.CharField(max_length=225)
    task_parentid = models.CharField(max_length=225)
    user_id = models.CharField(max_length=225)
    remind_time = models.DateTimeField
    task_isremind = models.BooleanField
    task_iscomplete = models.BooleanField
    task_completetime = models.DateTimeField
