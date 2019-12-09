# -*- coding: utf-8

import wx


class SimpleMenu(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(SimpleMenu, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_NEW, '&New')
        filemenu.Append(wx.ID_OPEN, '&Open')
        filemenu.Append(wx.ID_SAVE, '&Save')
        filemenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')

        filemenu.Append(wx.ID_ANY, 'I&mport', imp, 'Menu Import')

        qmi = wx.MenuItem(filemenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        qmi.SetBitmap(wx.Bitmap('exit.png'))
        filemenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((350, 250))
        self.SetTitle('Submenu')
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

