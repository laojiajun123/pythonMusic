import wx


app = wx.App()
window = wx.Frame(None, title = "IT自动化 - http://www.cnblogs.com/ItAuto/", size = (600,400))
panel = wx.Panel(window)
label = wx.StaticText(panel, label = "IT自动化", pos = (200,150))
window.Show(True)
app.MainLoop()