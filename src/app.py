<<<<<<< HEAD
from flask import Flask,jsonify, redirect, request
=======
from flask import Flask, render_template, request, redirect
>>>>>>> ef26ab79929c7cf81678988a04c78a2fb371fe40
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='mysql',          # Docker Compose service name
        user='myuser',
        password='mypassword',
        database='mydb'
    )

<<<<<<< HEAD
@app.route('/api/planets', methods=['GET'])
def get_planets():
    """Return a list of planets"""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, name, description FROM planets")
    planets = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(planets), 200


@app.route('/api/planets/<int:planet_id>/landmarks', methods=['GET'])
def get_landmarks(planet_id):
    """Return landmarks for a given planet"""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, name, type, coordinates 
        FROM landmarks 
        WHERE planet_id = %s
    """, (planet_id,))
    landmarks = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(landmarks), 200

@app.route('/api/routes', methods=['POST'])
def get_route():
    """Mock route calculation between landmarks"""
    data = request.get_json()
    start = data.get('start')
    end = data.get('end')

    # dummy example
    route = {
        "start": start,
        "end": end,
        "distance": "42 km",
        "estimated_time": "15 min"
    }
    return jsonify(route), 200
=======
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
>>>>>>> ef26ab79929c7cf81678988a04c78a2fb371fe40

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
