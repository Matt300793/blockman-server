import os
import sys
from flask import Flask, request, jsonify, make_response

# Ensures Vercel can see your 'blockmango' folder if you have one
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

# --- HELPING OLDER DEVICES ---
@app.after_request
def add_headers(response):
    # These headers tell the Poco C65 it's okay to accept the data
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# --- HOME ROUTE (Test this in your browser first) ---
@app.route('/')
def home():
    return jsonify({
        "status": "Server Active",
        "modder": "Evander_Mod",
        "note": "Use HTTPS for Vercel"
    })

# --- UPDATE CHECK ROUTE ---
# If this returns 200, the "No Internet" should stop
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
