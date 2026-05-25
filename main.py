# Добавили abort в импорт в первую строчку, иначе сервер выдаст ошибку
from flask import Flask, request, abort
import os

app = Flask(__name__)

KF = "unknownBLAME.lic"
usAg = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"

def load_keys():
    if not os.path.exists(KF):
        return []
    
    with open(KF, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

@app.route('/check', methods=['GET'])
def check_license():
    UsAg = request.headers.get('User-Agent')
    user_key = request.args.get('key')
    if UsAg != usAg:
        abort(403) # Теперь это сработает четко!
    
    valid_keys = load_keys()
    
    if user_key in valid_keys:
        return "VALID"
    return "INVALID"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


