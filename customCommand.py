import requests
actionUrl = 'http://35.188.38.8/lahacks'
import os
import dialogFlow
import pyrebase

config = {
	"apiKey": "AIzaSyBfSdJP-rwtyADckvIVe1GpO7sfGnkcpdo",
	"authDomain": "newagent-1-f8001.firebaseapp.com",
	"databaseURL": "https://newagent-1-f8001.firebaseio.com",
	"storageBucket": "newagent-1-f8001.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()



def writeToFile(filename,method,text):
	with open(filename, method) as file:
		file.write(text)

def clearFile(filename):
	try:
		os.remove(filename)
	except:
		f = open(filename, "w+")
		f.close()


class CustomCommand():
	def __init__(self,commandName):
		self.commandName = commandName
		self.linkedIntent = self.createIntent()
		self.reqs = []
		self.actions = []

	def createIntent(self):
		return 'intent xyz'

	def executeActions(self):
		for self.action in self.actions:
			dialogFlow.postQuery(self.action)

	def saveCommand(self):
		self.command = {
			"Name": self.commandName,
			"actions": self.actions,
			"linkedIntent": self.linkedIntent
		}

		db.child("commands").push(self.command)

