import wx

class SimpleExample(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(SimpleExample, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        self.count = 5

        self.toolbar = self.CreateToolBar()
        tundo = self.toolbar.AddTool(wx.ID_UNDO, '', wx.Bitmap('undo.png'))
        tredo = self.toolbar.AddTool(wx.ID_REDO, '', wx.Bitmap('redo.png'))
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.AddSeparator()
        texit = self.toolbar.AddTool(wx.ID_EXIT, '', wx.Bitmap('exit.png'))
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, texit)
        self.Bind(wx.EVT_TOOL, self.OnUndo, tundo)
        self.Bind(wx.EVT_TOOL, self.OnRedo, tredo)

        self.SetSize((350, 250))
        self.SetTitle('Undo Redo')
        self.Centre()

    def OnQuit(self, e):
        self.Close()

    def OnUndo(self, e):
        if self.count > 1 and self.count <=5:
            self.count -= 1
        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)
        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)

    def OnRedo(self, e):
        if self.count < 5 and self.count >=1:
            self.count += 1
        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)
        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_UNDO, True)

def main():
    app = wx.App()
    ex = SimpleExample(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()