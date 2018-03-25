from rest_framework import serializers
from server.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'user_id', 'user_nickname', 'user_email', 'user_pwd', 'wechat_openid', 'wechat_union', 'wechat_session_key', 'user_headimg', 'created')
        fields = ('user_nickname', 'user_email', 'user_pwd', 'wechat_openid', 'wechat_union',
                  'wechat_session_key', 'user_headimg', 'created')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('id', 'user_id', 'user_nickname', 'user_email', 'user_pwd', 'wechat_openid', 'wechat_union', 'wechat_session_key', 'user_headimg', 'created')
        fields = ('task_title', 'remind_time', 'task_isremind', 'task_iscomplete', 'task_completetime')