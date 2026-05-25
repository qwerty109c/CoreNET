from flask import Flask, request
import os

app = Flask(__name__)

# Имя файла, где будут храниться ключи (по одному на строку)
KEYS_FILE = "keys.txt"

def load_keys():
    # Если файла еще нет, возвращаем пустой список
    if not os.path.exists(KEYS_FILE):
        return []
    
    # Читаем файл и убираем лишние пробелы/переносы строк (\n)
    with open(KEYS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

@app.route('/check', methods=['GET'])
def check_license():
    user_key = request.args.get('key')
    
    # Загружаем актуальный список ключей из файла
    valid_keys = load_keys()
    
    if user_key in valid_keys:
        return "VALID"
    return "INVALID"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

