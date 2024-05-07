
from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configurations
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'Messi2005!',
    'database': 'cloudproject'
}

def connect_to_database():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

@app.route('/inf.html')
def display_student_data_inf():
    """Render the page to display student data."""
    return render_template('inf.html')

@app.route('/student_data')
def get_student_data():
    """Fetch student data from the database and return as JSON."""
    conn = connect_to_database()
    if not conn:
        return jsonify({'error': 'Could not connect to the database'})

    cursor = conn.cursor()

    # Fetch student data from the database
    query = "SELECT * FROM team"
    cursor.execute(query)
    student_data = cursor.fetchall()

    conn.close()

    # Convert data to JSON format and return
    return jsonify(student_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
