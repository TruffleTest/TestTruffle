import subprocess
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Vulnerability 1: SQL Injection
@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return str(cursor.fetchone())

# Vulnerability 2: Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    result = subprocess.call("ping -c 1 " + host, shell=True)
    return str(result)

# Vulnerability 3: XSS (Cross-Site Scripting)
@app.route('/greet')
def greet():
    name = request.args.get('name')
    return '<h1>Hello ' + name + '</h1>'

# Vulnerability 4: Hardcoded password
DB_PASSWORD = "SuperSecret123!"
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

# Vulnerability 5: Eval injection
@app.route('/calc')
def calc():
    expr = request.args.get('expr')
    result = eval(expr)
    return str(result)