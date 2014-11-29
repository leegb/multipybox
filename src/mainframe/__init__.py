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
import wx.lib.agw.aui as wxaui

import controllers
import views
import mainmodel

import maingui

@mvc.DynamicViewController
class MainFrame(maingui.MainFrame):

    # With tuple in the name we can define a "config" path for the variable
    def __init__(self, parent):
        maingui.MainFrame.__init__(self, parent)
        # wxPython 3.0.1.0 - Docking a pane will fail under windows withouth NATIVE_MINIFRAMES
        self.m_mgr.SetAGWFlags(self.m_mgr.GetAGWFlags() ^ wxaui.AUI_MGR_USE_NATIVE_MINIFRAMES)
        self.m_mgr.Update()
        self.Fit()

        self.model = mainmodel.MainModel()
