from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Shubhamw@1234',
    'database': 'urbanseva_db'
}

def get_db_connection():
    """Creates and returns a connection to the MySQL database."""
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    # Render the registration form
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        dob = request.form['dob']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        mobile_number = request.form['mobile_number']

        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return redirect(url_for('index'))

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Insert data into the database
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO users (name, dob, password, mobile_number) 
                VALUES (%s, %s, %s, %s)
            """, (name, dob, hashed_password, mobile_number))

            conn.commit()
            cursor.close()
            conn.close()

            flash("Account created successfully!", "success")
            return redirect(url_for('index'))

        except Exception as e:
            flash(f"An error occurred: {e}", "error")
            return redirect(url_for('index'))
    
    # If the method is GET, show the registration form
    return render_template('register.html')

@app.route('/test-db')
def test_db():
    """Tests the connection to the MySQL database."""
    try:
        conn = get_db_connection()
        conn.close()
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == '__main__':
    app.run(debug=True)
