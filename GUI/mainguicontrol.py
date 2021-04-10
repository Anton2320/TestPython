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

class MyAppWindowController_Message ( MyAppWindowController ):
	def createobject(self, objectname, objectlabel):
		self.parent.m_scrolledWindow_Dialog.GetSizer().Add(
				wx.StaticText(
					self.parent.m_scrolledWindow_Dialog, name=f"{objectname}", label=f"{objectlabel}"),
			    0, wx.ALL, 1)
		self.parent.m_scrolledWindow_Dialog.GetSizer().Layout()
		self.parent.Fit()

	def removeobject(self, objectname):
		if self.parent.m_scrolledWindow_Dialog.GetChildren():
			messagemarkedfordeletion = self.parent.m_scrolledWindow_Dialog.GetSizer().FindWindowByName(f"{objectname}").GetWindow()

	def loadmessages(self):
		pass

	def receivemesssage(self):
		pass

	def cleanparent(self):
		while self.parent.m_scrolledWindow_Dialog.GetChildren():
			parentsizer = self.parent.m_scrolledWindow_Dialog.GetSizer()
			messagemarkedfordeletion = parentsizer.GetItem(0).GetWindow()
			messagemarkedfordeletion.Hide()
			messagemarkedfordeletion.Destroy()
			self.parent.m_scrolledWindow_Dialog.GetSizer().Layout()
			self.parent.Fit()

class MyAppWindowController_Contact ( MyAppWindowController ):
	pass

		
if __name__ == '__main__': 
	app = wx.App() 
	mainGUI = MyAppWindow(None) 
	mainGUI.Show()
	WTF1 = MyAppWindowController_Message(mainGUI)
	WTF1.createobject("WTF", "WTF")
	WTF2 = MyAppWindowController_Message(mainGUI)
	WTF2.createobject("WTF2", "WTF2")
	#WTF2.removeobject("WTF2")
	WTF2.cleanparent()
	WTF2 = MyAppWindowController_Message(mainGUI)
	WTF2.createobject("WTF3", "WTF3")



	app.MainLoop()
	#MyAppWindowController_Message.createobject(mainGUI)
	# Thread(target = func1).start()
	# time.sleep(5)
	# Thread(target = func2).start()