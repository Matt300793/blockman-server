import os
import sys
from flask import Flask, request, jsonify, make_response

# Ensure Vercel can see your files
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

# --- HELPING OLDER DEVICES (CORS) ---
@app.after_request
def add_headers(response):
    # These headers tell the Poco C65 it is okay to accept the data
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    # Force the content type to JSON so the game doesn't think it's a website
    response.headers['Content-Type'] = 'application/json'
    return response

# --- HOME ROUTE ---
@app.route('/')
def home():
    return jsonify({
        "status": "Server Active",
        "modder": "Evander_Mod",
        "target_game": "Blockman Go 1.13.1",
        "note": "If you see this, the server is awake"
    })

# --- UPDATE CHECK ROUTE ---
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
            "description": "Latest version verified"
        }
    })

# --- LOGIN ROUTE ---
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

# --- CATCH-ALL ROUTE ---
@app.route('/<path:path>', methods=['GET', 'POST', 'OPTIONS'])
def catch_all(path):
    return jsonify({
        "code": 200, 
        "status": "Success", 
        "path": path
    })

# Do NOT use app.run() here for Vercel
        "data": {
            "hasUpdate": False,
            "version": "1.13.1",
            "downloadUrl": "",
            "description": "Latest version"
        }
    })

# --- LOGIN ROUTE ---
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

# --- CATCH-ALL ROUTE ---
# If the game asks for any other link, we say "200 OK"
@app.route('/<path:path>', methods=['GET', 'POST', 'OPTIONS'])
def catch_all(path):
    return jsonify({
        "code": 200, 
        "status": "Success", 
        "path": path
    })

# Do NOT use app.run() here
