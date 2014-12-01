from flask import Flask
from flask import make_response
from flask import request
from flask import abort
from flask import jsonify
from module.web.api.apiwhen import ApiWhen
from module.web.api.apinews import ApiNews

import jinja2
from flask import render_template

app = Flask(__name__, static_folder='module/web/static')
app.jinja_loader = jinja2.FileSystemLoader('module/web/templates')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/5w1h', methods = ['GET'])
def getInfo():
    data = {'hello'  : 'world'}
    resp = make_response(json.dumps(data), 200)
    return resp

@app.route('/api/randomnews', methods = ['GET'])
def getRandomNews():
    data = {'news'  : ApiNews.getRandomNews()}
    resp = make_response(jsonify(data), 200)
    return resp

@app.route('/api/when', methods = ['POST'])
def getWhen():
    if not request.form or not 'text' in request.form:
        abort(400)
    text = request.form['text']
    data = {'when' : ApiWhen.getWhen(text)}
    resp = make_response(jsonify(data), 200)
    return resp

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'wrong parameter'}), 400)

if __name__ == "__main__":
    app.run()