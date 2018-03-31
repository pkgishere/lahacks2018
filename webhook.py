from __future__ import print_function
import json
from flask import Flask,request,make_response,session
import logging
from logging import Formatter, FileHandler
from time import gmtime, strftime


app=Flask(__name__)
@app.route('/lahacks',methods=['POST'])
def LaHacks():
    app.logger.debug("Inside LAHACKS FUNSTION")
    req=request.get_json(silent=True, force=True)
    app.logger.debug("Request Json:"+ str(req))
    print(req)
    res=""
    res = processRequest(req)
    #if str(res).startswith("@EVENT="):
     #   res=makeWebhookResult("a", str(res.split('=')[1]), 1)
    #else:
     #   res = makeWebhookResult(res)

    res = json.dumps(res, indent=4)
    print(res)
    app.logger.debug("Response json:"+res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    app.logger.debug("Response json:"+ str(r))
    return r

def processRequest(req):
    if req['queryResult']['intent']['displayName'] == 'HiReply':
        print(req)
        print('hi')



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
    app.run(host='0.0.0.0',port=80,debug=True)
    app.logger.debug('Server stoped at '+strftime("%Y-%m-%d %H:%M:%S", gmtime()) )




