from flask import Flask, render_template, request, jsonify, redirect, url_for, session

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# Global variable to store table data
table_data = []

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username and password are correct
        if username == 'admin' and password == 'dinuth':
            session['logged_in'] = True
            return redirect(url_for('presenter_page'))
        else:
            return render_template('login_page.html', error='Invalid credentials')
    return render_template('login_page.html')

# Route for the presenter page (protected by login)
@app.route('/')
def presenter_page():
    if 'logged_in' in session:
        return render_template('presenter_page.html')
    else:
        return redirect(url_for('login'))

# Route to retrieve table data for the presenter page
@app.route('/get_table_numbers', methods=['GET'])
def get_table_numbers():
    return jsonify({'table_numbers': table_data})

# Route to clear table history
@app.route('/clear_table_history', methods=['POST'])
def clear_table_history():
    global table_data
    table_data = []  # Clear table data
    return jsonify({'status': 'success'})

# Route to add new table data
@app.route('/add_table_data', methods=['POST'])
def add_table_data():
    data = request.json
    table_data.insert(0, data)  # Add new data to the beginning of the list
    return jsonify({'status': 'success'})

# Route for the button page
@app.route('/button')
def button_page():
    return render_template('button_page.html')

# Route to logout and end session
@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Remove 'logged_in' session
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
