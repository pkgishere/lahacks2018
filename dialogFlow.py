
import requests
import random
apiUrl = 'https://api.dialogflow.com/v1/query?v=20150910'

headers = {
	"Authorization":"Bearer f788235201f44da3b4a569cbd5b39286",
	"Content-Type":"application/json"
}
def postQuery(text):
	payload = {
		"lang": "en",
		"query":text,
		"sessionId": "12345"
	}
	r = requests.post(apiUrl,data=payload)
	print(r.status_code)

def postIntent(name):
	intent = {
		"name": name,
		"displayName": name,
		"webhookState": 'WEBHOOK_STATE_ENABLED',
		"mlEnabled": True,
		"trainingPhrases": [

			{
				"name": "test intent 5",
				"type": "EXAMPLE",
				"parts": [
					{
						"text": "5",
						"entityType": "@sys.number",
						"alias": "number",
						"userDefined": False,
					}
				],
				"timesAddedCount": 5,
			}

		],
		"outputContexts": [
			{
				"name": name,
				"lifespanCount": 2,
				"parameters": {
					object
				}
			}
		],
		"resetContexts": False,
		"rootFollowupIntentName": "projects/9a3da9da-97d3-45c9-83c9-c806ec351f05/agent/intents/{}.".format(str(random.getrandbits(40))),
		"parentFollowupIntentName": string,
	}

	r = requests.post(apiUrl,data=intent)
	print(r.status_code)