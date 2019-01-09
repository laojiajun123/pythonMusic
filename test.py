# coding=utf-8
import urllib
import requests
from urllib import request

from urllib import parse

url = 'http://music.sonimei.cn/'
req = urllib.request.Request(url)
# html = requests.post(url).text


resp = urllib.request.urlopen(url)
html = resp.read()
print(html)
