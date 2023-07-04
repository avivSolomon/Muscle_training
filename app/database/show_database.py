import sqlite3


def show_database():
    conn = sqlite3.connect('muscle_training.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM User')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM TrainingProgram')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM Exercise')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM TrainingProgramExercise')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM Muscle')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM UserMuscle')
    print(cursor.fetchall())
    conn.close()


if __name__ == '__main__':
    show_database()
