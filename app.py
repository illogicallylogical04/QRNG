# app.py

from flask import Flask, request, jsonify
import QRNG  # Import the qrng function from QRNG.py

app = Flask(__name__)

@app.route('/generate_random_numbers', methods=['POST'])
def generate_random_numbers():
    max_value = int(request.json['max'])
    quantity = int(request.json['quantity'])
    
    # Call the qrng function directly
    random_numbers = qrng(max_value, quantity)
    
    return jsonify(random_numbers)

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
