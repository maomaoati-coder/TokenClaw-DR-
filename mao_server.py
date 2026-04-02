from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# The database of issued Distribution Rights (DR)
TOKEN_DB = "token_database.json"

def load_tokens():
    if os.path.exists(TOKEN_DB):
        with open(TOKEN_DB, 'r') as f:
            return json.load(f)
    return {}

@app.route('/verify', methods=['POST'])
def verify_token():
    """
    TokenClaw-DR: Core Verification Endpoint
    Intercepts and validates remote handshake requests.
    """
    data = request.json
    client_token = data.get("token")
    
    tokens = load_tokens()
    
    # Check if the token exists in our Distribution Rights database
    if client_token in tokens:
        user_info = tokens[client_token]
        print(f"\n[!] 授权成功: {user_info['client_name']} 正在请求 {user_info['asset']}")
        return jsonify({
            "status": "success",
            "message": "Authorization Granted",
            "client": user_info['client_name'],
            "asset": user_info['asset']
        }), 200
    else:
        print(f"\n[X] 拦截警告: 无效或过期的 Token 请求 -> {client_token}")
        return jsonify({
            "status": "failed",
            "message": "Invalid Token or Distribution Rights Expired"
        }), 403

if __name__ == '__main__':
    print("="*50)
    print("TokenClaw-DR Verification Hub is Starting...")
    print("Monitoring Distribution Rights on Port 5000")
    print("="*50)
    # Listen on all interfaces (0.0.0.0) to allow remote connections
    app.run(host='0.0.0.0', port=5000)
