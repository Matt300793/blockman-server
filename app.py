import os
from flask import Flask, request, jsonify
from blockmango import api  # This looks inside the /blockmango folder

app = Flask(__name__)

@app.route('/user/api/v1/login', methods=['POST'])
def login():
    # Example using the wrapper logic you put in api.py
    # data = api.get_player_info("12345")
    return jsonify({"code": 200, "status": "success"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
  
