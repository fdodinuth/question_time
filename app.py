from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global variable to store table data
table_data = []

# Route for the presenter page
@app.route('/')
def presenter_page():
    return render_template('presenter_page.html')

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

if __name__ == '__main__':
    app.run(debug=True)
