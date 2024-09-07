from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
CORS(app)
auth = HTTPBasicAuth()

# User data
users = {
    "admin": "Dinuth"  # Username and password
}

@auth.verify_password
def verify_password(username, password):
    if users.get(username) == password:
        return username

# In-memory store for table numbers and timestamps
table_numbers = []

@app.route('/')
def index():
    return render_template('button_page.html')

@app.route('/presenter')
@auth.login_required
def presenter():
    return render_template('presenter_page.html')

@app.route('/show_equation', methods=['POST'])
def show_equation():
    data = request.get_json()
    table_number = data.get('table_number')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table_numbers.append({'table_number': table_number, 'timestamp': timestamp})
    return jsonify({'status': 'success'})

@app.route('/get_table_numbers')
def get_table_numbers():
    return jsonify({'table_numbers': table_numbers})

if __name__ == '__main__':
    app.run()
