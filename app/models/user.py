from app.controller.training_program_controller import TrainingProgramController
from app.models.muscle import Muscle
import sqlite3
from datetime import date
from app.models.exercise import Exercise

class User:
    def __init__(self, user_id, name, email, password, height, weight, muscles=None, program=None):
        # Login Information
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        # bmi Information
        self.height = height
        self.weight = weight
        self.bmi = self.weight / ((self.height / 100) ** 2)
        # muscle and program information
        self.muscles = muscles
        self.program = program
        self.program_day = 0
        # save user
        self.save_user_data()

    def __str__(self):
        return "user_id: " + str(self.id) + "\n" + \
               "user_name: " + self.name + "\n" + \
               "height: " + str(self.height) + "\n" + \
               "weight: " + str(self.weight) + "\n" + \
               "bmi: " + str(self.bmi) + "\n" + \
               "muscles: " + str(self.muscles) + "\n" + \
               "program: " + str(self.program)


    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        self.save_user_data()

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
        self.save_user_data()

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
        self.save_user_data()

    @staticmethod
    def get_user_by_email(email):
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        if user is None:
            return None
        else:
            return [user[0], user[1], user[2], user[3], user[4], user[5]]

    def get_id(self):
        return self.id

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_bmi(self):
        return self.bmi

    def set_height(self, height):
        self.height = height
        self.save_user_data()

    def set_weight(self, weight):
        self.weight = weight
        self.save_user_data()

    def get_muscle(self, muscle_name):
        for cur_muscle in self.muscles:
            if cur_muscle.get_name() == muscle_name:
                return cur_muscle
        return None

    def get_muscle_list(self):
        return self.muscles

    def update_muscle(self, muscle_name, points, workout_date=date.today()):
        for cur_muscle in self.muscles:
            if cur_muscle.get_name() == muscle_name:
                cur_muscle.update_points(points, workout_date)
                return True
        return False

    def get_program(self):
        return self.program

    def set_program(self, program=None):
        if program is None:
            program = TrainingProgramController.standard_program_list[-1]\
                if self.bmi > 30 else ...
        self.program = program



    def workout(self):
        # get exercise_id, name, points from exercise table for each exercise in daily_workout
        # update points for each muscle in muscles table
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        c = conn.cursor()
        # get the day of the program
        c.execute("""SELECT day_of_training FROM TrainingProgram WHERE user_id = ?""",
                  (self.id,))
        self.program_day = c.fetchone()[0]
        c.execute("""SELECT Exercise.id, Exercise.value_points, Exercise.name
                    FROM Exercise
                    INNER JOIN DailyTrainingProgram ON Exercise.id = DailyTrainingProgram.exercise_id
                    INNER JOIN TrainingProgram ON DailyTrainingProgram.training_program_id = TrainingProgram.id
                    WHERE TrainingProgram.user_id = ? AND DailyTrainingProgram.day = ?""",
                  (self.id, self.program_day))
        daily_workout = c.fetchall()
        for exercise in daily_workout:
            print(exercise[2], end=', ')
        change_list = list(input(""" If there are exercises that did not perform as planned, 
                                    \nwrite down the names of the exercises here 
                                    \nSeparate with the help of "," between drill and drill if there are:""").split(","))
        user_muscles = Muscle.get_muscles_by_user_id(self.id)
        for exercise in daily_workout:
            if exercise[2] in change_list:
                Exercise.update_exe_details(exercise[0])
            exe_id, points, exe_name = exercise
            for muscle in user_muscles:
                if exe_name in TrainingProgramController.exercises_dict[muscle[1]]:
                    muscle_id = muscle[0]
                    update_points = muscle[2] + points
                    workout_date = date.today()
                    rest_date = Muscle.calculate_rest_time(points)
                    c.execute("""UPDATE Muscle SET points = ?, workout_date = ?, rest_date = ?
                                WHERE id = ?""",
                                (update_points, workout_date, rest_date, muscle_id))
                    c.execute("""INSERT INTO ExerciseHistory (user_id, exercise_id, workout_date)
                                VALUES (?, ?, ?)""",
                                (self.id, exe_id, workout_date))
                    conn.commit()
        conn.close()

    def save_user_data(self):
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        c = conn.cursor()
        c.execute("""UPDATE users SET name = ?, email = ?, password = ?, height = ?,
         weight = ?, bmi = ? WHERE user_id = ?""",
                  (self.name, self.email, self.password, self.height, self.weight, self.bmi, self.user_id))
        conn.commit()

    def print_val(self):
        for cur_muscle in self.muscles:
            print(cur_muscle)

if __name__ == '__main__':
    # check connection to database
    conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM users""")
    print(c.fetchall())
    conn.close()


