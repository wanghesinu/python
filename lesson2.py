# coding=utf-8
from urllib import request
from urllib import error

if __name__ == "__main__":
    # 一个不存在的连接
    url = "http://shop.enyuan.net/login"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
        #html = response.read().decode('utf-8')
        # print(html)
    except error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        elif hasattr(e, "reason"):
            print(e.reason)
