import psycopg2
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(database="flask_db", host="localhost", user="postgres", password="1523", port="5432")
    return conn

@app.route('/')
def index():
    conn = db_conn()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM USERS ORDER BY ID ASC''')
    data = cursor.fetchall()
    conn.close()
    cursor.close()

    return render_template('index.html', data=data)

@app.route('/create', methods=['POST'])
def create():
    conn =db_conn()
    cursor = conn.cursor()
    name = request.form['name']
    cursor.execute('''INSERT INTO USERS (name) VALUES (%s)''', (name,))
    conn.commit()
    conn.close()
    cursor.close()
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    conn = db_conn()
    cursor = conn.cursor()
    name = request.form['name']
    id = request.form['id']
    cursor.execute('''UPDATE USERS SET name=%s WHERE id=%s''', (name,id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    conn = db_conn()
    cursor = conn.cursor()
    id = request.form['id']
    cursor.execute('''DELETE FROM USERS WHERE id=%s''', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

app.run()