# -*- coding: utf-8

import wx

class MyPopupMenu(wx.Menu):
    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()
        self.parent = parent

        mmi = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        cmi = wx.MenuItem(self, wx.NewId(), 'Close')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)

    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()



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

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        self.SetSize((350, 250))
        self.SetTitle('Submenu')
        self.Centre()

    def OnQuit(self, e):
        self.Close()

    def OnRightDown(self, e):
        self.PopupMenu(MyPopupMenu(self), e.GetPosition())


def main():
    app = wx.App()
    ex = SimpleMenu(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

