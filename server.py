from flask import Flask, render_template
import json
import requests
from intuitlib.client import AuthClient
from intuitlib.enums import Scopes
from intuitlib.exceptions import AuthClientError
import os
from dotenv import dotenv_values
app = Flask(__name__)

config = dotenv_values(".env")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signIn():
    return None

@app.route('/signout')
def signOut():
    return None

@app.route('/dispatch')
def dispatch():
    return render_template('dispatch.html')

@app.route('/createorder', methods=['GET', 'POST'])
def orders():
    return render_template('orders.html')

@app.route('/history')
def history():
    return render_template('history')

@app.route('/order/<orderid>', methods=['GET','PUT','DELETE'])
def modify_order():
    return None

@app.route('/qbconnect')
def qb_connect():
    auth_client = AuthClient(
        config['INTUITCLIENTID'],
        config['INTUITCLIENTSECRET'],
        'https://us-central1-allstaterental.cloudfunctions.net/function-1',
        'sandbox'
    )
    url = auth_client.get_authorization_url([Scopes.ACCOUNTING])
    resp = requests.post(url)
    token = auth_client.get_bearer_token(resp.auth_code, realm_id=resp.realm_id)
    print(token)
    return None
