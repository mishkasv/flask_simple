from flask_security import auth_required
from flask import render_template

from app import app


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/good')
def good():
    return 'Everything will be good'