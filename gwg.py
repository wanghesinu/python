# -*- coding: UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = 'https://petitions.whitehouse.gov/'
    # 创建Request对象
    req = request.Request(url)
    # 传入创建好的Request对象
    response = request.urlopen(req)
    # 读取响应信息并解码
    html = response.read().decode('utf-8')
    # 打印信息
    # 创建Beautiful Soup对象
    soup = BeautifulSoup(html, 'lxml')
    tag = soup.find(attrs={"data-nid": "2545476"})
    print(tag.find("span", attrs={"class": "signatures-number"}).string)
