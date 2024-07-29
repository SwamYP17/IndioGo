"Create Database and Table:"
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='mysecretpassword'
)
conn.autocommit = True
cur = conn.cursor()

# Create database
cur.execute("CREATE DATABASE flight_status_db;")
cur.execute("CREATE USER flight_user WITH PASSWORD 'password';")
cur.execute("GRANT ALL PRIVILEGES ON DATABASE flight_status_db TO flight_user;")
cur.close()
conn.close()

# Connect to the new database
conn = psycopg2.connect(
    host='localhost',
    database='flight_status_db',
    user='flight_user',
    password='password'
)
cur = conn.cursor()

# Create flights table
cur.execute("""
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    flight_number VARCHAR(10) NOT NULL,
    status VARCHAR(20) NOT NULL,
    gate VARCHAR(10) NOT NULL
);
""")

# Insert mock data
cur.execute("""
INSERT INTO flights (flight_number, status, gate) VALUES
('AA123', 'On Time', 'A1'),
('DL456', 'On Time', 'B2'),
('UA789', 'On Time', 'C3');
""")

conn.commit()
cur.close()
conn.close()