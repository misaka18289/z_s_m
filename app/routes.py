from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return request.args.get('text')