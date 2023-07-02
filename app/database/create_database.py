import sqlite3


def create_tables():
    # Create a connection to the SQLite database
    conn = sqlite3.connect('muscle_training.db')
    cursor = conn.cursor()

    # Create User table
    cursor.execute('''
        CREATE TABLE Users (
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
        CREATE TABLE TrainingProgram (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            day_of_training INTEGER,
            duration_in_days INTEGER,
            FOREIGN KEY (user_id) REFERENCES User(user_id)
        )
    ''')

    # Create Exercise table
    cursor.execute('''
        CREATE TABLE Exercise (
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
        CREATE TABLE DailyTrainingProgram (
            training_program_id INTEGER,
            exercise_id INTEGER,
            day INTEGER,
            FOREIGN KEY (program_id) REFERENCES TrainingProgram(program_id),
            FOREIGN KEY (exercise_id) REFERENCES Exercise(exercise_id)
        )
    ''')

    # Create Muscle table
    cursor.execute('''
        CREATE TABLE Muscle (
            user_id INTEGER,
            name TEXT,
            points INTEGER,
            workout_date DATE,
            rest_time DATE,
            FOREIGN KEY (user_id) REFERENCES User(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE ExerciseHistory (
            user_id INTEGER,
            exercise_id INTEGER,
            workout_date DATE,
            FOREIGN KEY (user_id) REFERENCES User(id),
            FOREIGN KEY (exercise_id) REFERENCES Exercise(id)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_tables()


# users = [id, name, email, password, height, weight, bmi]
# muscles = [user_id, name, points, workout_date, rest_time]
# exercise = [id, prod, name, points, exercise_date]
# training_program = [user_id, name, duration, excercise_id, ]