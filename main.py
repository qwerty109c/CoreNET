from flask import Flask, request, abort  
import os

app = Flask(__name__)

KF = "unknownBLAME.lic"
usAg = "UsAgentCore-net3012.0daw"

def load_keys():
    if not os.path.exists(KF):
        return []
    with open(KF, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

@app.route('/check', methods=['GET'])
def check_license():
    UsAg = request.headers.get('User-Agent')
    user_key = request.args.get('key').strip()
    

    
    valid_keys = load_keys()
    
    if user_key in valid_keys:
        return "VALID"
    return "INVALID"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)



