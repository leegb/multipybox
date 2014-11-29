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
import models

import applets

class AppInfo(object):
    def __init__(self, maintab):
        self.maintab = maintab
        self.tabs = list()

    def AddTab(self, tab):
        self.tabs.append(tab)

    def DelTab(self, tab):
        self.tabs.remove(tab)
 
    def GetTabCount(self):
        return len(self.tabs)

@mvc.DynamicModel
class MainModel(object):
    def __init__(self, sendapplets=True):
        self.apps = dict()
        self.appcount = dict()
        self.appidx = dict()

        if sendapplets:
            self.SendApplets()

    @mvc.PubSend('mainmodel.applets')
    def SendApplets(self):
        return applets.applets

    def GetAppPage(self, appcls):
        return self.apps.get(appcls, None)

    def SetAppPage(self, appcls, page):
        self.apps[appcls] = page
        self.appcount[appcls] = 1

    def IncAppPage(self, appcls):
        count = self.appcount[appcls]
        self.appcount[appcls] = count + 1

    def GetAppPageCount(self, appcls):
        return self.appcount[appcls]
