# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan 11 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from YTDLClass import YTDL
import threading

###########################################################################
## Class MyFrame1
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 659,422 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.tUrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tUrl.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer2.Add( self.tUrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 2 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.bSet = wx.Button( self, wx.ID_ANY, u"Set this URL as current", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.bSet, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.bSet.Bind(wx.EVT_BUTTON, self.SetURL)


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 2 )

		gSizer3 = wx.GridSizer( 0, 4, 0, 0 )

		self.tFormat = wx.StaticText( self, wx.ID_ANY, u"Video Format", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tFormat.Wrap( -1 )

		gSizer3.Add( self.tFormat, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		FormatChoices = [ u"any", u"video/mp4", u"video/webm" ]
		self.cFormat = wx.ComboBox( self, wx.ID_ANY, u"any", wx.DefaultPosition, wx.DefaultSize, FormatChoices, 0 )
		gSizer3.Add( self.cFormat, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.cFormat.Bind(wx.EVT_COMBOBOX, self.SetList)

		self.tFps = wx.StaticText( self, wx.ID_ANY, u"FPS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tFps.Wrap( -1 )

		gSizer3.Add( self.tFps, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		FpsChoices = [ u"any", u"30", u"60" ]
		self.cFps = wx.ComboBox( self, wx.ID_ANY, u"any", wx.DefaultPosition, wx.DefaultSize, FpsChoices, 0 )
		gSizer3.Add( self.cFps, 0, wx.ALL|wx.EXPAND, 5 )

		self.cFps.Bind(wx.EVT_COMBOBOX, self.SetList)
		
		#self.cFps.Bind(wx.

		self.tRes = wx.StaticText( self, wx.ID_ANY, u"Resolution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tRes.Wrap( -1 )

		gSizer3.Add( self.tRes, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		resChoices = [ u"any", u"144p", u"360p", u"480p", u"720p", u"1080p" ]
		self.cRes = wx.ComboBox( self, wx.ID_ANY, u"any", wx.DefaultPosition, wx.DefaultSize, resChoices, 0 )
		gSizer3.Add( self.cRes, 0, wx.ALL|wx.EXPAND, 5 )

		self.cRes.Bind(wx.EVT_COMBOBOX, self.SetList)

		self.tCodec = wx.StaticText( self, wx.ID_ANY, u"VideoCodec", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tCodec.Wrap( -1 )

		gSizer3.Add( self.tCodec, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		codecChoices = []
		self.cCodec = wx.ComboBox( self, wx.ID_ANY, u"any", wx.DefaultPosition, wx.DefaultSize, codecChoices, 0 )
		gSizer3.Add( self.cCodec, 0, wx.ALL|wx.EXPAND, 5 )

		self.cCodec.Bind(wx.EVT_COMBOBOX, self.SetList)

		bSizer1.Add( gSizer3, 0, wx.EXPAND, 5 )

		gSizer31 = wx.GridSizer( 0, 2, 0, 0 )

		self.bRefresh = wx.Button( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.bRefresh, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.bRefresh.Bind(wx.EVT_BUTTON, self.SetList)		

		self.bDownload = wx.Button( self, wx.ID_ANY, u"Download selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.bDownload, 0, wx.ALL|wx.EXPAND, 5)
		
		self.bDownload.Bind(wx.EVT_BUTTON, self.DownloadItem)


		bSizer1.Add( gSizer31, 0, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticline2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		#self.m_treeListCtrl6 = wx.dataview.TreeListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.ListCtrl = wx.ListCtrl(self, size=wx.DefaultSize, style=wx.LC_REPORT|wx.BORDER_SUNKEN)
		
		"""self.ListCtrl.InsertColumn(0, u"Stream id", 125, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.ListCtrl.InsertColumn(1, u"resolution", 125, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.ListCtrl.InsertColumn(2, u"format", 125, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.ListCtrl.InsertColumn(3, u"FPS", 125, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.ListCtrl.InsertColumn(4, u"VideoCodec", 125, wx.ALIGN_LEFT, wx.COL_RESIZABLE)"""
		self.ListCtrl.InsertColumn(0, "Stream id")
		self.ListCtrl.InsertColumn(1, "Resolution")
		self.ListCtrl.InsertColumn(2, "format")
		self.ListCtrl.InsertColumn(3, "FPS")
		self.ListCtrl.InsertColumn(4, "VideoCodec")

		bSizer6.Add( self.ListCtrl, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticline3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )		
		bSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
			
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.dText = wx.StaticText( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.ST_ELLIPSIZE_MIDDLE )
		
		self.dText.Wrap( -1 )
		
		self.dText.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer5.Add( self.dText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )		
		
		self.pb = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.pb.SetValue( 0 )
		self.pb.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer5.Add( self.pb, 0, wx.ALL|wx.EXPAND, 5 )
				
		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )
				
		self.InitYTDL()
		self.yt.set_pb(self.pb, self.dText)
		#self.loop = asyncio.get_event_loop()
		#self.loop.run_forever()

	def SetList(self, event):
		self.SetFilters(None)
		self.ListCtrl.DeleteAllItems()
		lst = self.yt.get_streams_list()
		#for i in lst:
		#	print(i)
		#for audio : mime_type==[audio/mp4, audio/webm], acodec instead of vcodec
		
		#itag
		#mime_type
		#res
		#fps
		#vcodec
		for i in range(len(lst)):
			#print(lst[i])
			self.ListCtrl.InsertStringItem(i, str(lst[i].itag))
			self.ListCtrl.SetItem(i, 1, str(lst[i].resolution))
			self.ListCtrl.SetItem(i, 2, str(lst[i].mime_type))
			self.ListCtrl.SetItem(i, 3, str(lst[i].fps))
			item = ""
			try:
				item = lst[i].video_codec
			except:
				try:
					item = lst[i].audio_codec
				except:
					item = "Undefined"
			self.ListCtrl.SetStringItem(i, 4, str(item))			
		
	def DownloadItem(self, event):
		#print(self.ListCtrl.GetSelectedItemCount())
		#print(self.ListCtrl.GetNextSelected(-1))
		#print(self.ListCtrl.GetItem(0))
		#self.pb.SetValue(50)
		#self.Refresh(1)
		#time.sleep(5)
		#proc = Process(target=self.yt.download, args=[self.ListCtrl.GetNextSelected(-1), self.pb])
		#self.loop.create_task(self.yt.download(self.ListCtrl.GetNextSelected(-1)))
		threading.Thread(target=self.yt.download, args=[self.ListCtrl.GetNextSelected(-1)]).start()
		print("DownloadItem ENDED")
		#proc.start()
		#self.pb.Hide()
		
	def InitYTDL(self):
		self.yt = YTDL()
		
	def SetURL(self, event):
		#https://www.youtube.com/watch?v=C9OMIberEnI
		self.yt.set_url(self.tUrl.GetValue())
		self.SetList(None)
	
	def SetFilters(self, event):
		sup = {"res":self.cRes.GetValue(), "fps":self.cFps.GetValue(), "mime_type":self.cFormat.GetValue(), "vcodec":self.cCodec.GetValue()}
		self.yt.set_filters(sup)
		return

	def __del__(self):
		pass





# Run the program
if __name__ == "__main__":
	app = wx.App(False)
	frame = MainFrame(None)
	frame.Show()
	app.MainLoop()
