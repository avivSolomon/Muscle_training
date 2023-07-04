from datetime import date
import sqlite3
from app.database.create_database import DB_PATH


class Exercise:
    def __init__(self, training_program_id: int, day_of_training: int, name: str, intensity: int=1, sets=3, reps=10):
        self.id = self.get_new_exercise_id()
        self.training_program_id = training_program_id
        self.day_of_training = day_of_training
        self.name = name
        self.sets = sets
        self.reps = reps
        self.intensity = intensity
        self.value_points = round(sets * intensity * reps / 30)
        self.workout_date = date.today()
        self.save_exercise_data()

    def __str__(self):
        return "name: " + self.name + "\n" + \
               "sets: " + str(self.sets) + "\n" + \
               "reps: " + str(self.reps) + "\n" + \
               "intensity: " + str(self.intensity) + "\n" + \
               "value_points: " + str(self.value_points) + "\n" + \
               "workout_date: " + str(self.workout_date)

    def get_new_exercise_id(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT MAX(id) FROM Exercise")
        max_id = c.fetchone()[0]
        conn.close()
        return max_id + 1 if max_id is not None else 1

    def get_name(self):
        return self.name

    def get_sets(self):
        return self.sets

    def set_sets(self, sets):
        self.sets = sets
        self.save_exercise_data()

    def get_intensity(self):
        return self.intensity

    def set_intensity(self, intensity):
        self.intensity = intensity
        self.save_exercise_data()

    def get_reps(self):
        return self.reps

    def set_reps(self, reps):
        self.reps = reps
        self.save_exercise_data()

    def get_value_points(self):
        return self.value_points

    @staticmethod
    def update_exe_details(exercise_id):
        changes = input('enter the number of intensity, sets, and reps in this order,'
                        ' Separate by ",":  ').split(",")
        intensity, sets, reps = [int(num) for num in changes]
        # update exercise details in the database
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""UPDATE Exercise SET reps = ?, sets = ?, intensity = ? WHERE id = ?""",
                  (reps, sets, intensity, exercise_id))
        conn.commit()
        conn.close()
        return round(sets * intensity * reps / 30)

    def save_exercise_data(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO Exercise"
                  " (training_program_id, day_of_training, name,"
                  " intensity, sets, reps, value_points) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (self.training_program_id, self.day_of_training, self.name,
                   self.intensity, self.sets, self.reps, self.value_points))
        conn.commit()
        conn.close()


# Additional code for exercise-related functionality
