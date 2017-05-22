# -*- coding: UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'https://petitions.whitehouse.gov/'
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
    # 创建Beautiful Soup对象
    soup = BeautifulSoup(html, 'lxml')
    for i in soup.find_all(attrs={"data-nid": "2545476"}):
        one = i.find_all("span", attrs={"class": "signatures-number"})
        print(one[0].string)


#=""
