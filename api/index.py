import os
import sys
from flask import Flask, request, jsonify, Response

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

# --- 1. CONFIG PATH (The one from your log) ---
@app.route('/config/files/blockmods-config', methods=['GET', 'POST', 'OPTIONS'])
def blockmods_config():
    # We use a very compact JSON string with NO spaces
    raw_json = '{"code":200,"msg":"success","data":{"is_mod":true,"status":1}}'
    return Response(raw_json, status=200, mimetype='application/json')

@app.route('/user/api/v1/app/login', methods=['POST', 'OPTIONS'])
def login_route():
    # Compact login response
    raw_json = '{"code":200,"message":"success","data":{"userId":"10001","ticket":"v-mod-777"}}'
    return Response(raw_json, status=200, mimetype='application/json')


# --- 3. THE "SILENCE" HEADERS ---
@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    # This header is a secret trick to keep old Android connections stable
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route('/')
def home():
    return "Server Active - Evander Mod"

@app.route('/<path:path>', methods=['GET', 'POST', 'OPTIONS'])
def catch_all(path):
    return Response('{"code":200}', status=200, mimetype='application/json')
    
