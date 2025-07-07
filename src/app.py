from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='mysql',          # Docker Compose service name
        user='myuser',
        password='mypassword',
        database='mydb'
    )

@app.route('/')
def home():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT message FROM greetings")
    messages = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
    message = request.form['message']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO greetings (message) VALUES (%s)", (message,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
