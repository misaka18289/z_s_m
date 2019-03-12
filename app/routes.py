from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return request.args.get('text')

@app.route('/cat')
def cat():
    num=int(request.args.get('num'))
    return str(num+100)