from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='flight_status_db',
        user='flight_user',
        password='password'
    )
    return conn

@app.route('/flights', methods=['GET'])
def get_flights():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT flight_number, status, gate FROM flights;')
    flights = cur.fetchall()
    cur.close()
    conn.close()
    
    flight_list = []
    for flight in flights:
        flight_list.append({
            "flightNumber": flight[0],
            "status": flight[1],
            "gate": flight[2]
        })
    return jsonify(flight_list)

if __name__ == '__main__':
    app.run(debug=True)