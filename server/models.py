from django.db import models
import uuid


# Create your models here.


class User(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    user_id = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)  # 会员唯一ID
    user_nickname = models.CharField(max_length=255)  # 会员昵称
    user_email = models.EmailField(max_length=255)  # 会员绑定邮箱
    user_pwd = models.CharField(max_length=255)  # 会员账号密码
    wechat_openid = models.CharField(max_length=255)  # 会员微信标识
    wechat_union = models.CharField(max_length=255)  # 会员微信唯一标识
    wechat_session_key = models.CharField(max_length=255)  # 会员小程序秘钥
    user_headimg = models.CharField(max_length=255)  # 会员头像
    created = models.DateTimeField(auto_now_add=True)  # 会员注册时间


class Remind(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    user_id = models.UUIDField(editable=False, db_index=True)  # 提醒所属会员唯一ID
    task_id = models.UUIDField(editable=False, db_index=True)  # 提醒所属任务唯一ID
    remind_time = models.DateTimeField()  # 提醒时间
    remind_type = models.SmallIntegerField()  # 提醒类型，暂定：pre，on，over 三种，分别对应提前，当时，超时三种提醒
    isreminded = models.BooleanField(default=False)  # 是否已经提醒标记
    isdeal = models.BooleanField(default=False)  # 是否需要提醒标记
    remind_content = models.CharField(max_length=255)  # 提醒内容
    created = models.DateTimeField(auto_now_add=True)  # 记录创建时间
    updated = models.DateTimeField(auto_now=True)  # 记录最近一次修改时间


class Task(models.Model):
    id = models.BigAutoField(primary_key=True, db_index=True)
    task_id = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)  # 任务唯一ID
    task_title = models.CharField(max_length=255)  # 任务标题
    task_parentid = models.CharField(max_length=255)  # 父任务唯一ID
    user_id = models.CharField(max_length=255)  # 任务所属永无唯一ID
    remind_time = models.DateTimeField()  # 提醒时间
    task_isremind = models.BooleanField(default=False)  # 是否需要提醒
    task_iscomplete = models.BooleanField(default=False)  # 是否已完成，即任务关闭
    task_completetime = models.DateTimeField()  # 任务关闭时间
    created = models.DateTimeField(auto_now_add=True)  # 记录创建时间
    updated = models.DateTimeField(auto_now=True)  # 记录最近一次修改时间
