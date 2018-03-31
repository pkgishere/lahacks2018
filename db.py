import pyrebase

config = {
  "apiKey": "AIzaSyBfSdJP-rwtyADckvIVe1GpO7sfGnkcpdo",
  "authDomain": "newagent-1-f8001.firebaseapp.com",
  "databaseURL": "https://newagent-1-f8001.firebaseio.com",
  "storageBucket": "newagent-1-f8001.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

data = {"name": "Mortimer 'Morty' Smith"}
db.child("commands").update()