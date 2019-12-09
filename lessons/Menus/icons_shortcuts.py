# -*- coding: utf-8

import wx


APP_EXIT = 1

class SimpleMenu(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(SimpleMenu, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        qmi = wx.MenuItem(filemenu, APP_EXIT, '&Quit\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('exit.png'))
        filemenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((300, 200))
        self.SetTitle('Icons and Shortcuts')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = SimpleMenu(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
