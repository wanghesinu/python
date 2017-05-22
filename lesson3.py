# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    # 以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://shop.enyuan.net/login'
    head = {}
    # 写入User Agent信息
    head['User-Agent'] = 'test'
 # 创建Request对象
    req = request.Request(url, headers=head)
    # 传入创建好的Request对象
    response = request.urlopen(req)
    # 读取响应信息并解码
    html = response.read().decode('utf-8')
    # 打印信息
    print(html)
