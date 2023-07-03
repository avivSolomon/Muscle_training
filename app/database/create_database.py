import sqlite3


def create_tables():
    # Create a connection to the SQLite database
    conn = sqlite3.connect('muscle_training.db')
    cursor = conn.cursor()

    # Create User table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            password TEXT,
            height INTEGER,
            weight INTEGER,
            bmi REAL
        )
    ''')

    # Create TrainingProgram table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TrainingProgram (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            day_of_training INTEGER,
            duration INTEGER,
            FOREIGN KEY (user_id) REFERENCES Users(id)
        )
    ''')

    # Create Exercise table
    # Create Exercise table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Exercise (
            id INTEGER PRIMARY KEY,
            training_program_id INTEGER,
            day_of_training INTEGER,
            name TEXT,
            intensity INTEGER,
            sets INTEGER,
            reps INTEGER,
            value_points REAL,
            FOREIGN KEY (training_program_id) REFERENCES TrainingProgram(id),
            FOREIGN KEY (day_of_training) REFERENCES TrainingProgram(day_of_training)
        )
    ''')

    # Create TrainingProgramExercise table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DailyTrainingProgram (
            training_program_id INTEGER,
            exercise_id INTEGER,
            day INTEGER,
            FOREIGN KEY (training_program_id) REFERENCES TrainingProgram(id),
            FOREIGN KEY (exercise_id) REFERENCES Exercise(id)
        )
    ''')

    # Create Muscle table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Muscle (
            user_id INTEGER,
            name TEXT,
            points INTEGER,
            workout_date DATE,
            rest_time DATE,
            FOREIGN KEY (user_id) REFERENCES Users(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExerciseHistory (
            user_id INTEGER,
            exercise_id INTEGER,
            workout_date DATE,
            FOREIGN KEY (user_id) REFERENCES Users(id),
            FOREIGN KEY (exercise_id) REFERENCES Exercise(id)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def delete_all_data():
    conn = sqlite3.connect('muscle_training.db')
    c = conn.cursor()
    c.execute("DELETE FROM Users")
    c.execute("DELETE FROM TrainingProgram")
    c.execute("DELETE FROM Exercise")
    c.execute("DELETE FROM DailyTrainingProgram")
    c.execute("DELETE FROM Muscle")
    c.execute("DELETE FROM ExerciseHistory")
    conn.commit()
    conn.close()


def show_all_data():
    conn = sqlite3.connect('muscle_training.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Users")
    print(c.fetchall())
    c.execute("SELECT * FROM TrainingProgram")
    print(c.fetchall())
    c.execute("SELECT * FROM Exercise")
    print(c.fetchall())
    c.execute("SELECT * FROM DailyTrainingProgram")
    print(c.fetchall())
    c.execute("SELECT * FROM Muscle")
    print(c.fetchall())
    c.execute("SELECT * FROM ExerciseHistory")
    print(c.fetchall())
    conn.close()


if __name__ == '__main__':
    create_tables()
    conn = sqlite3.connect('muscle_training.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users')
    print(cursor.fetchall())
    # print(cursor.fetchall())
    # cursor.execute('INSERT INTO Users (name, email, password, height, weight, bmi) VALUES (?, ?, ?, ?, ?, ?)',
    #                ('John', 'john@gmail.com', '123456', 180, 80, 24.69))
    # cursor.execute('INSERT INTO Users (name, email, password, height, weight, bmi) VALUES (?, ?, ?, ?, ?, ?)',
    #                ('Jane', 'jane@gmail.com', '123456', 170, 60, 20.76))
    # cursor.execute('INSERT INTO Exercise (training_program_id, day_of_training, name, intensity, sets, reps, '
    #                'value_points) VALUES (?, ?, ?, ?, ?, ?, ?)',
    #                (1, 1, 'Push-ups', 1, 3, 10, 1))
    # cursor.execute('INSERT INTO Exercise (training_program_id, day_of_training, name, intensity, sets, reps, '
    #                'value_points) VALUES (?, ?, ?, ?, ?, ?, ?)',
    #                (1, 2, 'Pull-ups', 1, 3, 10, 1))
    # cursor.execute('INSERT INTO Exercise (training_program_id, day_of_training, name, intensity, sets, reps, '
    #                'value_points) VALUES (?, ?, ?, ?, ?, ?, ?)',
    #                (1, 3, 'Squats', 1, 3, 10, 1))
    # cursor.execute('INSERT INTO Exercise (training_program_id, day_of_training, name, intensity, sets, reps, '
    #                'value_points) VALUES (?, ?, ?, ?, ?, ?, ?)',
    #                (2, 1, 'Lunges', 1, 3, 10, 1))
    # cursor.execute('INSERT INTO Exercise (training_program_id, day_of_training, name, intensity, sets, reps, '
    #                'value_points) VALUES (?, ?, ?, ?, ?, ?, ?)',
    #                (2, 2, 'Crunches', 1, 3, 10, 1))
    # cursor.execute('INSERT INTO Exercise (training_program_id, day_of_training, name, intensity, sets, reps, '
    #                'value_points) VALUES (?, ?, ?, ?, ?, ?, ?)',
    #                (2, 3, 'Plank', 1, 3, 10, 1))
    # cursor.execute('INSERT INTO TrainingProgram (user_id, name, day_of_training, duration) VALUES (?, ?, ?, ?)',
    #                  (1, 'Beginner', 1, 3))
    # cursor.execute('INSERT INTO TrainingProgram (user_id, name, day_of_training, duration) VALUES (?, ?, ?, ?)',
    #                     (2, 'Advanced', 1, 3))
    # cursor.execute('INSERT INTO DailyTrainingProgram (training_program_id, exercise_id, day) VALUES (?, ?, ?)',
    #                (1, 1, 1))
    # cursor.execute('INSERT INTO DailyTrainingProgram (training_program_id, exercise_id, day) VALUES (?, ?, ?)',
    #                (1, 2, 2))
    # cursor.execute('INSERT INTO DailyTrainingProgram (training_program_id, exercise_id, day) VALUES (?, ?, ?)',
    #                (1, 3, 3))
    # cursor.execute('INSERT INTO DailyTrainingProgram (training_program_id, exercise_id, day) VALUES (?, ?, ?)',
    #                (2, 4, 1))
    # cursor.execute('INSERT INTO DailyTrainingProgram (training_program_id, exercise_id, day) VALUES (?, ?, ?)',
    #                (2, 5, 2))
    # cursor.execute('INSERT INTO DailyTrainingProgram (training_program_id, exercise_id, day) VALUES (?, ?, ?)',
    #                (2, 6, 3))
    # cursor.execute('INSERT INTO Muscle (user_id, name, points, workout_date, rest_time) VALUES (?, ?, ?, ?, ?)',
    #                (1, 'Chest', 0, '2020-01-01', '2020-01-02'))
    # cursor.execute('INSERT INTO Muscle (user_id, name, points, workout_date, rest_time) VALUES (?, ?, ?, ?, ?)',
    #                (1, 'Back', 0, '2020-01-01', '2020-01-02'))
    # cursor.execute('INSERT INTO Muscle (user_id, name, points, workout_date, rest_time) VALUES (?, ?, ?, ?, ?)',
    #                (2, 'Legs', 0, '2020-01-01', '2020-01-02'))
    # cursor.execute('INSERT INTO Muscle (user_id, name, points, workout_date, rest_time) VALUES (?, ?, ?, ?, ?)',
    #                (2, 'Abs', 0, '2020-01-01', '2020-01-02'))
    # cursor.execute('INSERT INTO ExerciseHistory (user_id, exercise_id, workout_date) VALUES (?, ?, ?)',
    #                (1, 1, '2020-01-01'))
    # cursor.execute('INSERT INTO ExerciseHistory (user_id, exercise_id, workout_date) VALUES (?, ?, ?)',
    #                (1, 2, '2020-01-01'))
    # cursor.execute('INSERT INTO ExerciseHistory (user_id, exercise_id, workout_date) VALUES (?, ?, ?)',
    #                (1, 3, '2020-01-01'))
    # cursor.execute('INSERT INTO ExerciseHistory (user_id, exercise_id, workout_date) VALUES (?, ?, ?)',
    #                (2, 4, '2020-01-01'))
    # cursor.execute('INSERT INTO ExerciseHistory (user_id, exercise_id, workout_date) VALUES (?, ?, ?)',
    #                (2, 5, '2020-01-01'))
    # cursor.execute('INSERT INTO ExerciseHistory (user_id, exercise_id, workout_date) VALUES (?, ?, ?)',
    #                (2, 6, '2020-01-01'))
    conn.commit()
    conn.close()

    show_all_data()
