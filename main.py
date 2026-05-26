from flask import Flask, request, abort  
import os

app = Flask(__name__)

usAg = "UsAgentCore-net3012.0daw"

def load_keys():
    keys_string = os.environ.get("LICENSE_KEYS", "")

    if keys_string:
        return [k.strip() for k in keys_string.split(",") if k.strip()]
    return []

@app.route('/check', methods=['GET'])
def check_license():
    UsAg = request.headers.get('User-Agent')
    user_key = request.args.get('key').strip()

    if UsAg != usAg:
        abort(403)

    valid_keys = load_keys()
    
    if user_key in valid_keys:
        return "VALID"
    return "INVALID"
@app.route('/')
def home():
    return """
    <html>
        <head><title>CoreNET Auth</title></head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1 style="color: #2c3e50;">Сервер авторизации CoreNET</h1>
            <p style="color: #7f8c8d;">Статус системы: <strong style="color: #27ae60;">ONLINE</strong></p>
        </body>
    </html>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)



