import sqlite3


def create_database():
    # create users table and muscles table and save it to data.db
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id integer PRIMARY KEY AUTOINCREMENT UNIQUE,
                user_name TEXT,
                height REAL,
                weight REAL
                )""")
    c.execute("""CREATE TABLE IF NOT EXISTS muscles (
                user_id INTEGER,
                muscle_name TEXT,
                points REAL,
                workout_date DATE,
                rest_time DATE,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
                )""")
    c.execute("""CREATE TABLE IF NOT EXISTS exercise_data (
                user_id INTEGER,
                exercise_name TEXT,
                points REAL,
                exercise_date DATE,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
                )""")
    conn.commit()
    conn.close()


def show_all_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    print(c.fetchall())
    c.execute("SELECT * FROM muscles")
    print(c.fetchall())
    c.execute("SELECT * FROM exercise_data")
    print(c.fetchall())
    conn.close()


def delete_all_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM users")
    c.execute("DELETE FROM muscles")
    conn.commit()
    conn.close()
