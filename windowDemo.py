import wx
# import MusicName
import time
from musicName import MusicName


def openfile(event):     # 定义打开文件事件
    music = MusicName()
    name = path_text.GetValue()
    music.getMusicBySinger(name,content_text)



        
def cleanFile(event):     # 定义打开文件事件
    path_text.Clear()
        


app = wx.App()
# window = wx.Frame(None, title = "IT自动化 - http://www.cnblogs.com/ItAuto/", size = (600,400))
# panel = wx.Panel(window)
# label = wx.StaticText(panel, label = "IT自动化", pos = (200,150))
frame = wx.Frame(None,title = "Gui Test Editor",pos = (1000,200),size = (500,400))

path_text = wx.TextCtrl(frame,pos = (5,5),size = (350,24))
open_button = wx.Button(frame,label = "下载",pos = (370,5),size = (50,24))
clear_button = wx.Button(frame,label = "重置",pos = (430,5),size = (50,24))
content_text= wx.TextCtrl(frame,pos = (5,39),size = (475,300),style = wx.TE_MULTILINE)

open_button.Bind(wx.EVT_BUTTON,openfile)
clear_button.Bind(wx.EVT_BUTTON,cleanFile)

# window.Show(True)
frame.Show()
app.MainLoop()