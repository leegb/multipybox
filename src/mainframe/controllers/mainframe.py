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
from .. import aboutdialog
import wx
import wx.lib.agw.aui as wxaui


if True:
    # @DynBind.EVT_BUTTON.Button.AboutDialog
    @mvc.DynBind.EVT_TOOL.Tool.AboutDialog
    @mvc.DynBind.EVT_MENU.MenuItem.AboutDialog
    def OnEventAboutDialog(self, event):
        event.Skip()
        if True:
            dialog = aboutdialog.AboutDialog(self)
            dialog.ShowModal()


if True:
    nbstyle = wxaui.AUI_NB_BOTTOM | \
              wxaui.AUI_NB_TAB_SPLIT | \
              wxaui.AUI_NB_TAB_MOVE | \
              wxaui.AUI_NB_CLOSE_ON_ALL_TABS | \
              wxaui.AUI_NB_DRAW_DND_TAB | \
              wxaui.AUI_NB_SMART_TABS | \
              0

    @mvc.DynBind.EVT_TREE_ITEM_ACTIVATED.TreeCtrl.Apps
    def OnEventTreeItemActivatedApps(self, event):
        treeItemId = self.m_treeCtrlApps.GetSelection()
        treeItemData = self.m_treeCtrlApps.GetItemData(treeItemId)
        appname, tabname, appcls = treeItemData.GetData()

        apppage = self.model.GetAppPage(appcls)
        if apppage:
            found, index = self.m_nbapps.FindTab(apppage)
            if not found:
                apppage = None
            else:
                self.model.IncAppPage(appcls)

        if not apppage:
            apppage = wxaui.AuiNotebook(self.m_nbapps, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, nbstyle)

            # Add a page to hold all instances of this applet
            self.m_nbapps.AddPage(apppage, appname)
            self.model.SetAppPage(appcls, apppage)

        count = self.model.GetAppPageCount(appcls)
        app = appcls(apppage)

        if hasattr(app, 'GetTabName'):
            tabname = app.GetTabName(count)
        elif tabname:
            tabname = tabname + '-' + str(count)
        else:
            tabname = appname

        apppage.AddPage(app, tabname)
        apppage.Refresh()
        apppage.Update()

if False:
    #@mvc.DynBind('lib.agw.aui').EVT_AUINOTEBOOK_PAGE_CLOSED.NB.Apps
    def OnEventNotebookPageCloseApps(self, event):
        event.Skip()
