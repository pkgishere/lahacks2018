from twilio.rest import Client
import csv
import threading
from utils import *
import re
account_sid = "ACfadbe3cf4b03b2c737a94020a8cf9141"
auth_token = "d7725184e3b83b0a88b7fbc5575d51fd"
alertText = "Test"
audio = "https://handler.twilio.com/twiml/EHe45a1ba014ca37097d55512a3743ec0a"
client = Client(account_sid, auth_token)
twillioNum = '+19704091393'
numbers = '9082976813'.split(',')


def call(number,url):
	call = client.calls.create(
		to=number,
		from_= twillioNum,
		url=url
	)
	taskLog(number,'Call sent')

def text(number,text):
	client.api.account.messages.create(
		to=number,
		from_=twillioNum,
		body=text)
	taskLog(number,'Message sent')

class Alert(threading.Thread):
	def __init__(self,number):
		threading.Thread.__init__(self)
		self.number = number

	def run(self):
		taskLog(self.number, 'Alerting..')
		try:
			call(self.number,audio)
		except Exception as e:
			print(self.number,e)
		try:
			text(self.number,alertText)
		except Exception as e:
			print(self.number,e)





