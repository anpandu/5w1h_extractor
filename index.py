from flask import Flask
from flask import Response
from flask import json


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/5w1h', methods = ['GET'])
def getInfo():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://anpandu.com'
    return resp

if __name__ == "__main__":
    app.run()