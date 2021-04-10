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
					self.parent, name=f"m_staticText_{objectname}", label=f"{objectlabel}"),
			    0, wx.ALL, 1)
		self.parent.GetSizer().Layout()
		self.parent.GetParent().Fit()

	def removeobject(self, objectname):
		if self.parent.GetChildren():
			messagemarkedfordeletion = self.parent.FindWindowByName(f"m_staticText_{objectname}")
			messagemarkedfordeletion.Hide()
			messagemarkedfordeletion.Destroy()

class MyAppWindowController_Message ( MyAppWindowController_StaticText ):
	def loadmessages(self, sender):
		self.cleanmessages()
		messages = messageloader.loadmessagesfromDB(sender);
		for message in messages:
			pass
		return messages

	def updatemesssages(self):
		pass

	def cleanmessages(self):
		while self.parent.GetChildren():
			messagemarkedfordeletion = self.parent.GetSizer().GetItem(0).GetWindow()
			messagemarkedfordeletion.Hide()
			messagemarkedfordeletion.Destroy()
			self.parent.GetSizer().Layout()
			self.parent.GetParent().Fit()

class MyAppWindowController_Contact ( MyAppWindowController_StaticText ):
	def createobject(self, objectname, objectlabel):
		newobject = wx.StaticText(self.parent, name=f"m_staticText_{objectname}", label=f"{objectlabel}")
		self.parent.GetSizer().Add(newobject, 0, wx.ALL, 1)
		self.parent.GetSizer().Layout()
		self.parent.GetParent().Fit()
		newobject.Bind( wx.EVT_LEFT_DOWN, self.onContactClick )

	def onContactClick(self, event):
		print("something clicked!")

		
if __name__ == '__main__': 
	app = wx.App() 
	mainGUI = MyAppWindow(None) 
	mainGUI.Show()

	TSTV1 = MyAppWindowController_Message(mainGUI.m_scrolledWindow_Contacts)
	TSTV1.createobject("localhost", "localhost")	

	TSTV1 = MyAppWindowController_Message(mainGUI.m_scrolledWindow_Dialog)
	TSTV1.createobject("TSTV", "TSTV")
	TSTV2 = MyAppWindowController_Message(mainGUI.m_scrolledWindow_Dialog)
	TSTV2.createobject("TSTV2", "TSTV2")
	TSTV2.cleanmessages()
	TSTV3 = MyAppWindowController_Message(mainGUI.m_scrolledWindow_Dialog)
	TSTV3.createobject("TSTV3", "TSTV3")
	#TSTV3.removeobject("TSTV3")



	app.MainLoop()
	#MyAppWindowController_Message.createobject(mainGUI)
	# Thread(target = func1).start()
	# time.sleep(5)
	# Thread(target = func2).start()