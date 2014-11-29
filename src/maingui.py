# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from wx.lib.agw.aui import AuiNotebook
import wx
import wx.xrc
import wx.aui

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT|wx.aui.AUI_MGR_LIVE_RESIZE|wx.aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE)
		
		self.m_treeCtrlApps = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_HAS_BUTTONS|wx.TR_SINGLE )
		self.m_mgr.AddPane( self.m_treeCtrlApps, wx.aui.AuiPaneInfo() .Left() .CaptionVisible( False ).CloseButton( False ).Gripper().Dock().Resizable().FloatingSize( wx.DefaultSize ).DockFixed( False ).Floatable( False ) )
		
		self.m_nbapps = AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_CLOSE_ON_ALL_TABS|wx.aui.AUI_NB_DEFAULT_STYLE|wx.aui.AUI_NB_TAB_SPLIT|wx.aui.AUI_NB_WINDOWLIST_BUTTON )
		self.m_mgr.AddPane( self.m_nbapps, wx.aui.AuiPaneInfo() .Center() .CaptionVisible( False ).CloseButton( False ).Gripper().Dock().Resizable().FloatingSize( wx.DefaultSize ).DockFixed( False ).Floatable( False ) )
		
		
		self.m_nblog = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_BOTTOM|wx.aui.AUI_NB_CLOSE_ON_ALL_TABS|wx.aui.AUI_NB_DEFAULT_STYLE|wx.aui.AUI_NB_TAB_MOVE|wx.aui.AUI_NB_TAB_SPLIT )
		self.m_mgr.AddPane( self.m_nblog, wx.aui.AuiPaneInfo() .Bottom() .CaptionVisible( False ).CloseButton( False ).Gripper().Dock().Resizable().FloatingSize( wx.DefaultSize ).DockFixed( False ).Floatable( False ) )
		
		
		self.m_auiToolBar1 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_toolAboutDialog = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"About ...", wx.ArtProvider.GetBitmap( u"priv/icons/information.png", wx.ART_OTHER ), wx.NullBitmap, wx.ITEM_NORMAL, u"About ...", u"Show the About Dialog", None ) 
		
		self.m_tool9 = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_INFORMATION, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar1.Realize()
		self.m_mgr.AddPane( self.m_auiToolBar1, wx.aui.AuiPaneInfo().Top().CaptionVisible( False ).CloseButton( False ).Gripper().Dock().Resizable().FloatingSize( wx.DefaultSize ).DockFixed( False ).Layer( 10 ).ToolbarPane() )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItemAboutDialog = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"&About ...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemAboutDialog )
		
		self.m_menubar1.Append( self.m_menu1, u"&Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.m_mgr.Update()
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	

###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebookAbout = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panelAbout = wx.Panel( self.m_notebookAbout, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextAppNameVersion = wx.StaticText( self.m_panelAbout, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextAppNameVersion.Wrap( -1 )
		bSizer10.Add( self.m_staticTextAppNameVersion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextCopyright = wx.StaticText( self.m_panelAbout, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextCopyright.Wrap( -1 )
		bSizer10.Add( self.m_staticTextCopyright, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_hyperlinkURL = wx.HyperlinkCtrl( self.m_panelAbout, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
		bSizer10.Add( self.m_hyperlinkURL, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_panelAbout.SetSizer( bSizer10 )
		self.m_panelAbout.Layout()
		bSizer10.Fit( self.m_panelAbout )
		self.m_notebookAbout.AddPage( self.m_panelAbout, u"About", True )
		
		bSizer8.Add( self.m_notebookAbout, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_buttonClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_buttonClose, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PanelAboutDocument
###########################################################################

class PanelAboutDocument ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrlDocument = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_AUTO_URL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer111.Add( self.m_textCtrlDocument, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer111 )
		self.Layout()
		bSizer111.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class TextPad
###########################################################################

class TextPad ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.m_toolNew = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_NORMAL_FILE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolOpen = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolSave = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolSaveAs = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar1.AddSeparator()
		
		self.m_toolFind = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_FIND, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolFindAndReplace = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_FIND_AND_REPLACE, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar1.AddSeparator()
		
		self.m_toolAbout = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( wx.ART_INFORMATION, wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar1.Realize() 
		
		bSizer1.Add( self.m_toolBar1, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_textCtrlText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1.Add( self.m_textCtrlText, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
	
	def __del__( self ):
		pass
	

