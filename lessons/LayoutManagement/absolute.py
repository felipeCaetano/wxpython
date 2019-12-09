import wx


class Exemple(wx.Frame):
    def __init__(self, parent, title):
        super(Exemple, self).__init__(parent, title=title, size=(350, 300))
        self.rotunda = None
        self.bardejov = None
        self.mincol = None
        self.InitUI()
        self.Centre()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('gray')
        self.LoadImages()

        self.mincol.SetPosition((20, 20))
        self.bardejov.SetPosition((40, 160))
        self.rotunda.SetPosition((170, 50))

    def LoadImages(self):
        self.mincol = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("resources/images/anvisa.jpg", wx.BITMAP_TYPE_ANY))
        self.bardejov = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("resources/images/farmasys_logo.png", wx.BITMAP_TYPE_ANY))
        self.rotunda = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("resources/images/top.png", wx.BITMAP_TYPE_ANY))


def main():
    app = wx.App()
    ex = Exemple(None, title='Absolute positioning')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()


