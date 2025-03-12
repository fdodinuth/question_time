from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
CORS(app)
auth = HTTPBasicAuth()

# User data
users = {
    "admin": "admin"  # Username and password
}

@auth.verify_password
def verify_password(username, password):
    if users.get(username) == password:
        return username

# In-memory store for table numbers, questions, names, and timestamps
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
    table_number = data.get('table_number') if not data.get('anonymous') else 'Anonymous'
    name = data.get('name') if not data.get('anonymous') else 'Anonymous'
    question = data.get('question')
    timestamp = datetime.now().strftime('%H:%M:%S')  # Only time
    table_numbers.append({'table_number': table_number, 'question': question, 'name': name, 'timestamp': timestamp})
    return jsonify({'status': 'success'})

@app.route('/get_table_numbers')
def get_table_numbers():
    return jsonify({'table_numbers': table_numbers})

@app.route('/clear_table_history', methods=['POST'])
@auth.login_required
def clear_table_history():
    global table_numbers
    table_numbers = []  # Clear the list
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
