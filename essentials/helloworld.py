import wx

app = wx.App()
frame = wx.Frame(parent=None, title='Hello World Exemple", 
text = wx.StaticText(parent=frame, label="Hello World")

frame.Show()
app.MainLoop()
