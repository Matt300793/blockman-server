import os
from flask import Flask, request, jsonify
# This imports the User class you just showed me
from blockmango.user import User 

app = Flask(__name__)

# This route handles your entire list of User APIs automatically
@app.route('/user/api/v1/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_bmg_api(path):
    print(f"📡 Request: {request.method} -> /user/api/v1/{path}")
    
    # Custom response for the 'user/info' path in your list
    if path == "user/info":
        return jsonify({
            "code": 200,
            "data": {
                "userId": "777777",
                "nickName": "Evander_Dev",
                "gcube": 999999,
                "gold": 1000000
            }
        })

    # Default success response for the rest of the list
    return jsonify({"code": 200, "message": "success", "data": {}})

if __name__ == '__main__':
    # Required for Koyeb Free Tier
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
