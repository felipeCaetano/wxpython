import wx
import wx.lib.buttons as buttons


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()

    def InitUI(self):
        panel = wx.Panel(self)

        bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (25, 25))
        btn1 = buttons.ThemedGenBitmapTextButton(panel, -1, bmp, label='Information', style=wx.TOP, size=(110, 90), pos=(50, 10))
        btn2 = wx.Button(panel, -1, label='information', pos=(50, 120), size=(100, 90), style=wx.TOP)
        btn2.SetBitmap(bmp, wx.TOP)


def main():
    app = wx.App()
    ex = MyFrame(None, title='Review')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
