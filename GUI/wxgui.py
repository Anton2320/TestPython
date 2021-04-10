# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyAppWindow
###########################################################################

class MyAppWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DHT messenger", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 400,400 ), wx.DefaultSize )

		bSizer_Main = wx.BoxSizer( wx.HORIZONTAL )

		bSizer_LeftPanel = wx.BoxSizer( wx.VERTICAL )

		bSizer_Nickname = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText_Nickname = wx.StaticText( self, wx.ID_ANY, u"Enter Your Nickname", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_staticText_Nickname.Wrap( -1 )

		bSizer_Nickname.Add( self.m_staticText_Nickname, 0, wx.ALL, 5 )

		self.m_textCtrl_Nickname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_Nickname.Add( self.m_textCtrl_Nickname, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button_Nickname = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_Nickname.Add( self.m_button_Nickname, 0, wx.ALL, 5 )


		bSizer_LeftPanel.Add( bSizer_Nickname, 0, wx.EXPAND, 5 )

		self.m_scrolledWindow_Contacts = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow_Contacts.SetScrollRate( 5, 5 )
		bSizer_Contacts = wx.BoxSizer( wx.VERTICAL )


		self.m_scrolledWindow_Contacts.SetSizer( bSizer_Contacts )
		self.m_scrolledWindow_Contacts.Layout()
		bSizer_Contacts.Fit( self.m_scrolledWindow_Contacts )
		bSizer_LeftPanel.Add( self.m_scrolledWindow_Contacts, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer_Main.Add( bSizer_LeftPanel, 1, wx.EXPAND, 5 )

		bSizer_RightPanel = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_DialogWith = wx.StaticText( self, wx.ID_ANY, u"Dialog with: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_DialogWith.Wrap( -1 )

		bSizer_RightPanel.Add( self.m_staticText_DialogWith, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_scrolledWindow_Dialog = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow_Dialog.SetScrollRate( 5, 5 )
		bSizer_Dialog = wx.BoxSizer( wx.VERTICAL )


		self.m_scrolledWindow_Dialog.SetSizer( bSizer_Dialog )
		self.m_scrolledWindow_Dialog.Layout()
		bSizer_Dialog.Fit( self.m_scrolledWindow_Dialog )
		bSizer_RightPanel.Add( self.m_scrolledWindow_Dialog, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer_Send = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_SendField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_WORDWRAP )
		bSizer_Send.Add( self.m_textCtrl_SendField, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button_Send = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_Send.Add( self.m_button_Send, 0, wx.ALL, 5 )


		bSizer_RightPanel.Add( bSizer_Send, 0, wx.EXPAND, 5 )


		bSizer_Main.Add( bSizer_RightPanel, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_Main )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


