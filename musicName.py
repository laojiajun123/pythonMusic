import urllib
import urllib.request
import re
import time
import urllib.parse
import json

class MusicName():

    # basePath = '/Users/laojiajun/Desktop/project/pythonProject/music/'
    basePath = 'E:\\music\\'
    url = 'http://music.sonimei.cn/'

    # sdfsdf

    def getSingerData(self,name,type,num):
        print("开始请求数据======")

        form = {
            'input': name,
            'filter': 'name',
            'type': type,
            'page': num
        }
        print("页数=========="+str(num))

        carNum = len(name)
        contentNum = 40
        # 添加type字符数
        contentNum = contentNum+len(form['type'])
        if carNum>0:
            contentNum+= (carNum-1)*9

        # 先处理百位
        jisuanNum=1
        while jisuanNum<100:
            jisuanNum=jisuanNum*10
            if num / jisuanNum >= 1:
                contentNum = contentNum + 1

        print("页面头数据=========="+str(contentNum))

        headers = {
            'Accept': 'application/json, text/javascript,*/*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'music.sonimei.cn',
            'Origin': 'http://music.sonimei.cn',
            'Content-Length': contentNum,
            # 54 两个字
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
            'X-Requested-With': 'XMLHttpRequest'
        }

        jshtml = self.postUrl(form,headers,self.url)

        # dataLen = len(jshtml['data'])
        # if dataLen>0:
        #     for datalist in jshtml['data']:
        #         path = basePath + datalist['title']+"_"+datalist['author']+".mp3"
        #         print("保存路径======" + path)
        #         urllib.request.urlretrieve(datalist['url'], path)

        # if jshtml['data'][0]['title'] == form['input']:
        #     path = basePath+ jshtml['data'][0]['title'] + ".mp3"
        #     print("保存路径======" + path)
        #     print("保存链接======" + jshtml['data'][0]['title'])
        #     print(jshtml['data'][0]['url'])
        #     urllib.request.urlretrieve(jshtml['data'][0]['url'], path)

        return jshtml

    currlist = []

    def parseData(self,jshtml,cont):
        print("开始解析======")

        # 校验文件夹
        # print("数据"+self.os.basePath.isdir())



        dataLen = len(jshtml['data'])
        if dataLen > 0:
            reStr = jshtml['data'][0]['title']
            if re.match(".*"+reStr+".*",jshtml['data'][1]['title'])==None or re.match(".*"+reStr+".*",jshtml['data'][2]['title'])==None:
                for datalist in jshtml['data']:
                    cont.AppendText("下载====="+datalist['title']+"\n")
                    print("初始数据-=======" + datalist['title'])
                    if datalist['title'] not in self.currlist:
                        path = self.basePath + datalist['title'] + "_" + datalist['author'] + ".mp3"
                        print("保存路径jshtml['data'][0]======" + path)
                        self.currlist.append(datalist['title'])
                        urllib.request.urlretrieve(datalist['url'], path)
            else:
                cont.AppendText("下载"+jshtml['data'][0]['title']+"\n")
                print("初始数据-=======" + jshtml['data'][0]['title'])
                path = self.basePath + jshtml['data'][0]['title'] + "_" + jshtml['data'][0]['author'] + ".mp3"
                print("保存路径======" + path)
                self.currlist.append(jshtml['data'][0]['title'])
                urllib.request.urlretrieve(jshtml['data'][0]['url'], path)



    def getAllMusicBySinger():
        num =1
        print('开始时间')
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        while num<30:
            dataList = getSingerData("林俊杰", "kugou", num)
            # time.sleep(5)
            if len(dataList)>0:
                parseData(dataList)
            else:
                break
            num = num+1

        print('结束时间')
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        return

    # 返回接口参数
    def postUrl(self,param,headers,url):
        print("开始请求======")
        form_data = urllib.parse.urlencode(param)
        form_data = form_data.encode('UTF-8')

        req = urllib.request.Request(url, data=form_data, headers=headers, method='POST')

        resp = urllib.request.urlopen(req)
        html = resp.read().decode('utf8')
        jshtml = json.loads(html)
        print(jshtml['data'])
        return jshtml



    def getMusicBySinger(self,muName,contentDO):
        num =1
        contentDO.AppendText('开始\n')
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        while num<30:
            dataList =self.getSingerData(muName, "kugou", num)
            # time.sleep(5)
            if len(dataList)>0:
                self.parseData(dataList,contentDO)
            else:
                break
            num = num+1

        contentDO.AppendText('结束\n')
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        return

