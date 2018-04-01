import pyrebase

config = {
  "apiKey": "AIzaSyBfSdJP-rwtyADckvIVe1GpO7sfGnkcpdo",
  "authDomain": "newagent-1-f8001.firebaseapp.com",
  "databaseURL": "https://newagent-1-f8001.firebaseio.com",
  "storageBucket": "newagent-1-f8001.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

d = {
	"name": "Dance",
	"call": "intent1",
	"actions":[
		{
			"actionName":"actionCall"
		},
		{
			"actionName": "actionCall"
		},
		{
			"actionName": "actionCall"
		}
	]
}

commands = [d,d,d]
db.child("commands").push(commands)
