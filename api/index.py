import os
import sys
from flask import Flask, request, jsonify, make_response

# Add current directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    # Adding this tells the game the data is finished sending
    response.headers['Connection'] = 'keep-alive'
    response.headers['Keep-Alive'] = 'timeout=5, max=100'
    return response

@app.route('/')
def home():
    return jsonify({
        "status": "Server Active",
        "modder": "Evander_Mod",
        "target_game": "Blockman Go 1.13.1"
    })

@app.route('/update/check', methods=['GET', 'POST', 'OPTIONS'])
@app.route('/version.xml', methods=['GET'])
@app.route('/config/update', methods=['GET', 'POST'])
def check_update():
    return jsonify({
        "code": 200,
        "message": "success",
        "data": {
            "hasUpdate": False,
            "version": "1.13.1",
            "downloadUrl": "",
            "description": "Latest version"
        }
    })

@app.route('/user/api/v1/app/login', methods=['POST', 'OPTIONS'])
def handle_login():
    return jsonify({
        "code": 200,
        "message": "success",
        "data": {
            "userId": "10001",
            "accessToken": "v-mod-token-777",
            "userName": "Evander_Mod"
        }
    })

@app.route('/<path:path>', methods=['GET', 'POST', 'OPTIONS'])
def catch_all(path):
    return jsonify({
        "code": 200, 
        "status": "Success", 
        "path": path
    })
    
