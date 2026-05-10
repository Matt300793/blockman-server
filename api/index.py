import os
import sys
from flask import Flask, request, jsonify

# This line is crucial for Vercel to find your other folders
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# This MUST be at the top level for Vercel to see it
app = Flask(__name__)

# --- HOME ROUTE ---
@app.route('/')
def home():
    return jsonify({
        "status": "Server Active",
        "owner": "Evander_Mod",
        "target_game": "Blockman Go 1.13.1"
    })

# --- UPDATE CHECK ROUTE ---
# Handles the common paths older BMG versions use to check for updates
@app.route('/update/check', methods=['GET', 'POST'])
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
@app.route('/user/api/v1/app/login', methods=['POST'])
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
# This ensures that ANY link the game hits returns a 200 OK status
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    return jsonify({
        "code": 200, 
        "status": "Handled", 
        "requested_path": path
    })

# IMPORTANT: Do NOT add app.run() here for Vercel
