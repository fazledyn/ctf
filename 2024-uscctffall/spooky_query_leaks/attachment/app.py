from flask import Flask, render_template, request, redirect, session, g
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'REDACTED'

DATABASE = 'challenge.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = get_db().cursor()
        try:
            cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{generate_password_hash(password)}')")
            #                INSERT INTO users (username, password) VALUES ('rabid', '123'); UPDATE users SET password='scrypt:32768:8:1$U0zDMrX1iYDwd6Yf$af4b2ac49d2bfc5a009573524f1d2dcb4e8d2e7e9684335ddbecb44dfc3ea975f8e2fa9a75b8fa6490ada68e5f625f8a02c0832b4015e5b8ef0a83732e039dc3' WHERE name='admin';--
            get_db().commit()
            return redirect('/login')
        except sqlite3.IntegrityError:
            return "Username already taken."

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = get_db().cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']
            return redirect('/dashboard')
        else:
            return "Invalid credentials."

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')

    username = session['username']
    cursor = get_db().cursor()

    if username == 'admin':
        cursor.execute("SELECT flag FROM flags")
        flag = cursor.fetchone()['flag']
        return render_template('dashboard.html', username=username, flag=flag)

    return render_template('dashboard.html', username=username, flag=None)

if __name__ == '__main__':
    app.run(debug=False)
