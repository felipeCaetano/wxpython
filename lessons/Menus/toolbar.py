import wx

class SimpleExample(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(SimpleExample, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        vbox = wx.BoxSizer(wx.VERTICAL)

        toolbar1 = wx.ToolBar(self)
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('new.png'))
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('open.png'))
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('save.png'))
        toolbar1.Realize()

        toolbar2 = self.CreateToolBar()
        qtool = toolbar2.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('exit.png'))
        toolbar2.Realize()

        vbox.Add(toolbar1, 0, wx.EXPAND)
        vbox.Add(toolbar2, 0, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        self.SetSize((350, 250))
        self.SetTitle('Simple Toolbar')
        self.Centre()

    def OnQuit(self, e):
        self.Close()

def main():
    app = wx.App()
    ex = SimpleExample(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()