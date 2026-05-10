from flask import Flask, request, jsonify
import sys
import os

# Define 'app' at the top level
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "Server is running"})

# Add your other routes below...


# --- NEW: UPDATE CHECK ROUTE ---
# This matches common patterns for Blockman Go update checks
@app.route('/update/check', methods=['GET', 'POST'])
@app.route('/version.xml', methods=['GET'])
@app.route('/config/update', methods=['GET', 'POST'])
def check_update():
    # We return a JSON that says 'no update' or 'latest version'
    return jsonify({
        "code": 200,
        "message": "success",
        "data": {
            "hasUpdate": False,
            "version": "1.13.1",
            "downloadUrl": "",
            "description": "No update needed"
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
# If the game asks for a URL we didn't plan for, it still gets a 'Success'
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"code": 200, "status": "ok", "path": path})
            "nickName": "Evander_Mod",
            "level": 100
        }
    })

# --- CATCH-ALL ROUTE ---
@app.route('/user/api/v1/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    return jsonify({"code": 200, "message": "Handled by Vercel", "path": path})

# DO NOT add app.run() for Vercel
