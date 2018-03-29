import requests


class HttpHelper:

    @staticmethod
    def http_get(url, args=None, headers=None):

        if args is None:
            args = []

        if headers is None:
            headers = []

        r = requests.get(url, params=args, headers=headers)
        return r

    @staticmethod
    def http_post(url, args=None, headers=None):

        if args is None:
            args = []

        if headers is None:
            headers = []

        r = requests.post(url, data=args, headers=headers)
        return r

    @staticmethod
    def wx_get(url, args=None):

        return HttpHelper.http_get(url, args)

    @staticmethod
    def wx_post(url, args=None):

        return HttpHelper.http_post(url, args)
