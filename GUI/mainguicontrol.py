#from anton.DHTmessenger.DBConnection.messageloader import MyDHTMessage
from wxgui import *
from abc import ABCMeta, ABC, abstractmethod
import requests
import time
from threading import Thread
		
class MyAppWindowController(MyAppWindow):
	def __init__(self, parent):
		self.parent = parent

	@abstractmethod
	def createobject(self):
		pass

	@abstractmethod
	def removeobject(self):
		pass

class MyAppWindowController_StaticText ( MyAppWindowController ):
	def createobject(self, objectname, objectlabel):
		self.parent.GetSizer().Add(
				wx.StaticText(
					self.parent, name=f"{objectname}", label=f"{objectlabel}"),
			    0, wx.ALL, 1)
		self.parent.GetSizer().Layout()
		self.parent.GetParent().Fit()

	def removeobject(self, objectname):
		if self.parent.m_scrolledWindow_Dialog.GetChildren():
			messagemarkedfordeletion = self.parent.GetSizer().FindWindowByName(f"{objectname}").GetWindow()

class MyAppWindowController_Message ( MyAppWindowController_StaticText ):
	def loadmessages(self):
		pass

	def receivemesssage(self):
		pass

	def cleanmessages(self):
		while self.parent.GetChildren():
			messagemarkedfordeletion = self.parent.GetSizer().GetItem(0).GetWindow()
			messagemarkedfordeletion.Hide()
			messagemarkedfordeletion.Destroy()
			self.parent.GetSizer().Layout()
			self.parent.GetParent().Fit()

class MyAppWindowController_Contact ( MyAppWindowController_StaticText ):
	pass

		
if __name__ == '__main__': 
	app = wx.App() 
	mainGUI = MyAppWindow(None) 
	mainGUI.Show()
	WTF1 = MyAppWindowController_Message(mainGUI.m_scrolledWindow_Dialog)
	WTF1.createobject("TSTV", "TSTV")
	WTF2 = MyAppWindowController_Message(mainGUI.m_scrolledWindow_Dialog)
	WTF2.createobject("TSTV2", "TSTV2")
	#WTF2.removeobject("WTF2")
	WTF2.cleanmessages()
	WTF2 = MyAppWindowController_Message(mainGUI.m_scrolledWindow_Dialog)
	WTF2.createobject("TSTV3", "TSTV3")



	app.MainLoop()
	#MyAppWindowController_Message.createobject(mainGUI)
	# Thread(target = func1).start()
	# time.sleep(5)
	# Thread(target = func2).start()