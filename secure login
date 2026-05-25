from flask import Flask, render_template_string, request, redirect, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "secretkey"

# Database connection
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password BLOB
)
""")

# Home Page
@app.route('/')
def home():
    if 'user' in session:
        return f"Welcome {session['user']}! <br><a href='/logout'>Logout</a>"
    return redirect('/register')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash password using bcrypt
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Store in database
        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hashed))
        conn.commit()

        return "Registration Successful! <a href='/login'>Login</a>"

    return render_template_string('''
        <h2>Register</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Register">
        </form>
    ''')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Fetch user from database
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        if user:
            stored_password = user[1]

            # Verify password
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                session['user'] = username
                return redirect('/')

        return "Invalid Username or Password"

    return render_template_string('''
        <h2>Login</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    ''')

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# Run application
if __name__ == '__main__':
    app.run(debug=True)
