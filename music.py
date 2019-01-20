import urllib
import urllib.request
import re
# from urllib import request

import requests
import urllib.parse
import json

# data = bytes(urllib.parse.urlencode({'name': '沙龙','type':'kugou'}), encoding='utf8')

form = {
    'input': '光年之外',
    'filter': 'name',
    'type': 'kugou',
    'page': 1
}

form_data = urllib.parse.urlencode(form)
form_data = form_data.encode('UTF-8')
headers = {
    'Accept': 'application/json, text/javascript,*/*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': 72,
    # 54 两个字
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'http://music.sonimei.cn/'
req = urllib.request.Request(url, data=form_data, headers=headers, method='POST')

resp = urllib.request.urlopen(req)
html = resp.read().decode('utf8')
jshtml = json.loads(html)
print(jshtml['data'])

if jshtml['data'][0]['title'] == form['input']:
    path = '/Users/laojiajun/' + jshtml['data'][0]['title'] + ".mp3"
    print("保存路径======" + path)
    print("保存链接======" + jshtml['data'][0]['title'])
    print(jshtml['data'][0]['url'])
    urllib.request.urlretrieve(jshtml['data'][0]['url'], path)

