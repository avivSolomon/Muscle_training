from app.models.exercise import Exercise
import sqlite3


class TrainingProgram:

    def __init__(self, program_id, user_id, name, day_of_training, duration, exercises):
        self.id = program_id
        self.user_id = user_id
        self.day_of_training = day_of_training
        self.name = name
        self.duration = duration
        self.exercises = exercises
        self.save_program_data()



    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def add_exercise(self, name, intensity:int, sets=3, reps=10):
        self.exercises.append(Exercise(name, intensity, sets, reps))

    def remove_exercise(self, exercise):
        if exercise in self.exercises:
            self.exercises.remove(exercise)

    def get_exercises(self):
        return self.exercises

    def get_exercise_of_program(self, exercise_name):
        for cur_exercise in self.exercises:
            if cur_exercise.get_name() == exercise_name:
                return cur_exercise
        return None

    # def clear_exercises(self):
    #     self.exercises = []

    def get_program_details(self):
        program_details = f"Training Program: {self.name}\n"
        program_details += f"Duration: {self.duration} days\n"
        program_details += "Exercises:\n"

        for exercise in self.exercises:
            program_details += f"- {exercise.get_name()}\n"

        return program_details

    def save_program_data(self):
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        c = conn.cursor()
        c.execute("INSERT INTO training_program (user_id, name, day_of_training, duration) VALUES (?, ?, ?, ?)",
                  (self.user_id, self.name, self.day_of_training, self.duration))
        conn.commit()
        conn.close()



