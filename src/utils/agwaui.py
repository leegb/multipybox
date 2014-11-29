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
# If imported before wx in any other module it will replace wx.aui with wx.lib.agw.aui
# and help for example with the GUI definitions from wxFormBuilder
# Theoretically agw.aui is a drop in replacement, but ... some things do not fit 100%
# and therefore ... it's not being used right now, being the manual approach favoured

import wx
import wx.lib.agw.aui
setattr(wx, 'aui', wx.lib.agw.aui)
import sys
sys.modules['wx.aui'] = wx.lib.agw.aui

# Create SetFlags in "new" AuiManager - wxFormBuilder will call it
setattr(wx.lib.agw.aui.AuiManager, 'SetFlags', getattr(wx.lib.agw.aui.AuiManager, 'SetAGWFlags'))
