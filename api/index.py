import os
import sys
from flask import Flask, request, jsonify

# FIX: This allows the script to find the 'blockmango' folder in the root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from blockmango.user import User

app = Flask(__name__)

# --- LOGIN ROUTE ---
@app.route('/user/api/v1/app/login', methods=['POST'])
def handle_login():
    data = request.json
    print(f"Login attempt for: {data.get('uid')}")
    
    return jsonify({
        "code": 200,
        "message": "success",
        "data": {
            "userId": data.get('uid') or "10001",
            "accessToken": "v-mod-token-777",
            "userName": "Evander_Mod"
        }
    })

# --- USER INFO ROUTE ---
@app.route('/user/api/v1/user/info', methods=['GET', 'POST'])
def get_user_info():
    return jsonify({
        "code": 200,
        "data": {
            "gold": 1000000,
            "gcube": 999999,
            "diamond": 50000,
            "nickName": "Evander_Mod",
            "level": 100
        }
    })

# --- CATCH-ALL ROUTE ---
@app.route('/user/api/v1/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    return jsonify({"code": 200, "message": "Handled by Vercel", "path": path})

# DO NOT add app.run() for Vercel
