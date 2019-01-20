# coding=utf-8
import urllib
import requests
import re
from urllib import request

from urllib import parse

url = 'http://music.sonimei.cn/'
req = urllib.request.Request(url)
# html = requests.post(url).text


resp = urllib.request.urlopen(url)
html = resp.read()
ss = ['1111(live)','2222']
print(re.match(".*111111.*","1111111"))
print(html)
