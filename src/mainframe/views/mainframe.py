#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
################################################################################
# 
#  Copyright (C) 2014 Daniel Rodriguez
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
import utils.mvc as mvc
import wx

if True:
    def __init__(self, *args, **kwargs):

        # Operating System Details for column sizes
        winDC = wx.ClientDC(self)

        uisizes = {
            self.m_treeCtrlApps: (25, 40),
            self.m_nbapps: (120, 40),
            self.m_nblog: (150, 20),
        }

        for ctrl, minsize in uisizes.iteritems():
            minw, minh = minsize
            w, h = winDC.GetTextExtent('A' * minw)
            h *= minh
            self.SetMinSize(wx.Size(w, h))
            self.SetSize(wx.Size(w, h))

        self.m_mgr.Update()
        self.Fit()

if True:
    @mvc.PubRecv('mainmodel.applets')
    def OnMainModelAppList(self, applets):
        self.m_treeCtrlApps.DeleteAllItems()
        self.m_treeCtrlApps.AddRoot('Applets')
        rootitem = self.m_treeCtrlApps.GetRootItem()
        for name, tabname, appcls in applets:
            itemdata = wx.TreeItemData((name, tabname, appcls))
            self.m_treeCtrlApps.AppendItem(parent=rootitem, text=name, data=itemdata)
