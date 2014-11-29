#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
################################################################################
# 
# Copyright (C) 2014 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
import os
import utils.mvc as mvc
import wx

wildcard = "Text Files (*.txt)|*.text|" \
           "All files (*.*)|*.*"

def CheckModified(self, save=True):
    if self.m_textCtrlText.IsModified():
        answer = wx.MessageBox(
            'Text has been edited. Do you want to save it?',
            'Text Modified',
            wx.YES_NO | wx.CANCEL, parent=self)

        if answer == wx.CANCEL:
            return False

        if answer == wx.YES:
            if not self.DoLoadSave(save=save):
                return False

    return True

def DoLoadSave(self, save=True, saveas=False):
    # Show a dialog to choose the file
    loadsave = wx.SAVE if save else wx.OPEN
    dlg = wx.FileDialog(
        self, message='Choose a file',
        defaultDir=os.getcwd(),
        defaultFile='',
        wildcard=wildcard,
        style=loadsave)

    if dlg.ShowModal() != wx.ID_OK:
        return False

    self.fname = dlg.GetPath()

    if save:
        self.m_textCtrlText.SaveFile(self.fname)
    else:
        self.m_textCtrlText.LoadFile(self.fname)

if True:
    @mvc.DynBind.EVT_TOOL.Tool.New
    def OnEventNew(self, event):
        event.Skip()
        if not CheckModified(save=True):
            return
            
        self.m_textCtrlText.Clear()

if True:
    @mvc.DynBind.EVT_TOOL.Tool.Open
    def OnEventOpen(self, event):
        event.Skip()

        if not CheckAndSaveModified(save=True):
            return

        DoLoadSave(save=False)

if True:
    @mvc.DynBind.EVT_TOOL.Tool.Save
    def OnEventSaveAs(self, event):
        event.Skip()

        if not CheckAndSaveModified(save=True):
            return

        DoLoadSave(save=False)
