from flask import Flask, request
import os

app = Flask(__name__)

KEYS_FILE = "unknownBLAME.lic"

def load_keys():
    if not os.path.exists(KEYS_FILE):
        return []
    
    with open(KEYS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

@app.route('/check', methods=['GET'])
def check_license():
    user_key = request.args.get('key')
    
    valid_keys = load_keys()
    
    if user_key in valid_keys:
        return "VALID"
    return "INVALID"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

