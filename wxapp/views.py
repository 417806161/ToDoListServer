from utils.services.HttpHelper import HttpHelper
from ToDoListServer import localconfig
from django.http import HttpResponse
from server.models import User
import time
from .WXBizDataCrypt import WXBizDataCrypt
import json


# Create your views here.
def login(request):
    if request.method == 'GET':
        # 获取用户 openid 的请求url，从小程序文档获取
        url = 'https://api.weixin.qq.com/sns/jscode2session'

        # 请求数据
        request_data = {
            'appid': localconfig.WXAPP['appid'],  # 小程序的appid
            'secret': localconfig.WXAPP['secret'],  # 小程序的 secret
            'js_code': request.GET['code'],  # 从小程序传递过来的授权 code ，用于获取用的 openid 等信息
            'grant_type': 'authorization_code'  # 默认值
        }

        # 发出请求，json 格式化返回数据
        r = HttpHelper.wx_get(url, request_data).json()

        # todo 这里需要判断一下，如果请求出错了怎么办
        openid = r['openid']
        session_key = r['session_key']
        # 提前5分钟让 session_key 过期掉
        expires_in = r['expires_in'] + int(time.time()) - 300

        # todo 这里要对传过来的数据进行一次签名认证

        # 解析前端传递过来的加密数据
        pc = WXBizDataCrypt(localconfig.WXAPP['appid'], session_key)
        user_info = pc.decrypt(request.GET['encryptedData'], request.GET['iv'])

        # 抽离出用户信息，为用户注册
        user = User(
            user_nickname = user_info['nickName'],
            user_headimg= user_info['avatarUrl'],
            # user_gender= user_info['gender'],
            wechat_openid= openid,
            wechat_session_key= session_key,
            # wechat_session_key_expire= expires_in
        )

        user.save()


        # 解析获得的数据
        wechat_data = json.dumps(user_info)

        return HttpResponse(wechat_data)
