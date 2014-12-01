from flask import Flask
from flask import Response
from flask import json
from module.webservice.api.apiwhen import ApiWhen
from module.dataprovider import MDP

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/5w1h', methods = ['GET'])
def getInfo():
    data = {
        'hello'  : 'world'
    }
    resp = Response(json.dumps(data), status=200, mimetype='application/json') #resp.headers['Link'] = 'http://anpandu.com'
    return resp

@app.route('/api/when', methods = ['GET'])
def apiWhen():
    text = MDP.get5w1h([6])[1].text
    data = {'when' : ApiWhen.getWhen(text)}
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run()