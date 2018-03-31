from __future__ import print_function
import json
from flask import Flask,request,make_response,session
import logging
from logging import Formatter, FileHandler
from time import gmtime, strftime
import botInterface as bot


app=Flask(__name__)

@app.route('/lahacks',methods=['POST'])
def LaHacks():
	app.logger.debug("Inside LAHACKS FUNCTION")
	req=request.get_json(silent=True, force=True)
	app.logger.debug("Request Json:"+ str(req))
	pprint(req)
	res = processRequest(req)

	app.logger.debug("Response json:\n"+res)

	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'

	return r
#
# hi = {
#   "responseId": "7934e93d-2a82-4f9a-a79c-2038f8947bce",
#   "queryResult": {
#     "queryText": "move 10 units left",
#     "parameters": {
#       "number": 10,
#       "direction": "left"
#     },
#     "allRequiredParamsPresent": true,
#     "fulfillmentText": "Ok, moving left 10 units",
#     "fulfillmentMessages": [
#       {
#         "text": {
#           "text": [
#             "Ok, moving left 10 units"
#           ]
#         }
#       }
#     ],
#     "outputContexts": [
#       {
#         "name": "projects/aiclub-a0691/agent/sessions/efa53a48-984a-4386-80f7-7a7bffe11df4/contexts/movement",
#         "lifespanCount": 2,
#         "parameters": {
#           "direction": "left",
#           "direction.original": "left",
#           "number": 10,
#           "number.original": "10"
#         }
#       }
#     ],
#     "intent": {
#       "name": "projects/aiclub-a0691/agent/intents/4b19b3f6-7d2a-4e42-ad8b-37fd8b9adc5f",
#       "displayName": "Move"
#     },
#     "intentDetectionConfidence": 1,
#     "diagnosticInfo": {
#       "webhook_latency_ms": 3
#     },
#     "languageCode": "en"
#   },
#   "webhookStatus": {
#     "code": 3,
#     "message": "Webhook call failed. Error: Webhook response was empty."
#   }
# }

def parseMove(context):
	direction = context['parameters']['direction']
	number = int(context['parameters']['number'])
	print('bot',bot.move(direction, number))
	return buildResponse('Ok, moving {} units {}!'.format(number, direction))

def parseRotation(context):
	direction = context['parameters']['direction']
	number = int(context['parameters']['number']['amount'])

	print('bot',bot.rotate(direction, number))
	return buildResponse('Ok, moving {} units {}!'.format(number, direction))

def parseLED(context):
	state = context['parameters']['LedState']
	print('bot',bot.setLED(state))
	return buildResponse('Ok, turning LED {}!'.format(state))

def processRequest(req):

	pprint(req)
	intent = req['queryResult']['intent']['displayName']
	print(intent)
	if intent == 'HiReply':
		return buildResponse('this is a hiReply')
	elif intent == 'Move':
		# bot.move()
		context = detectcontext(req,'movement')
		return parseMove(context)

	elif intent == 'LedTrigger':
		context = detectcontext(req,'ledtrigger')
		return parseLED(context)


	elif intent == 'Rotate':
		context = detectcontext(req,'rotate')
		return parseRotation(context)

	else:
		return buildResponse("Not sure what you're saying?")


def detectcontext(req,targetContext):
	for context in req['queryResult']['outputContexts']:
		contextName = context['name'].split('/')[-1]
		if contextName == targetContext:
			return context
	return None

def pprint(text):
	print(json.dumps(text,indent=4))

def buildResponse(reply):

	response = {
		"fulfillmentText":reply
	}

	return json.dumps(response)



if __name__ == '__main__':
	file_handler = FileHandler('output.log')
	handler = logging.StreamHandler()
	file_handler.setLevel(logging.DEBUG)
	handler.setLevel(logging.DEBUG)
	file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	app.logger.addHandler(handler)
	app.logger.addHandler(file_handler)
	app.logger.warning('Server started at '+strftime("%Y-%m-%d %H:%M:%S", gmtime()) )
	app.run(host='0.0.0.0',port=80,debug=False)
	app.logger.debug('Server stoped at '+strftime("%Y-%m-%d %H:%M:%S", gmtime()) )




