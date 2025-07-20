from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

@app.route('/random')
def get_random():
    min_val = int(os.getenv("MIN_VALUE", "1"))
    max_val = int(os.getenv("MAX_VALUE", "100"))
    number = random.randint(min_val, max_val)
    return jsonify({
        "random_number": number,
        "range": f"{min_val}-{max_val}",
        "app_name": os.getenv("APP_NAME", "MyApp"),
        "environment": os.getenv("ENVIRONMENT", "dev"),
        "secret_token": os.getenv("SECRET_TOKEN", "not_set")
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

