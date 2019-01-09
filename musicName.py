import urllib
from urllib import request
import re
import requests
from urllib import parse

import json

form = {
    'key': '张学友'
}

form_data = urllib.parse.urlencode(form)
# form_data = form_data.encode('utf8')
# print(form_data)
headers = {
    # 'Accept': 'application/json, text/javascript,*/*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

url = 'http://music.taihe.com/search?'+form_data
# req = request.Request(url, data=form_data,headers=headers, method='GET')

resp = request.urlopen(url)
html = resp.read().decode('utf8')
# jshtml = json.loads(html)
print(html)
# for ss in jshtml['data']:
#     if ss['title'] == form['input']:
#         path = '/Users/laojiajun/' + ss['title'] + ".mp3"
#         print("保存路径======" + path)
#         print("保存链接======" + ss['title'])
#         urllib.request.urlretrieve(ss['url'], path)
