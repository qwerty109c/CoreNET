from flask import Flask, request

app = Flask(__name__)

# Ваши лицензионные ключи
VALID_KEYS = ["CoreNet-KEY-1", "CoreNet-KEY-2"]

@app.route('/check', methods=['GET'])
def check_license():
    user_key = request.args.get('key')
    if user_key in VALID_KEYS:
        return "VALID"
    return "INVALID"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
