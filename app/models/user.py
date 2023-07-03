from app.controller.training_program_controller import TrainingProgramController
from app.models.muscle import Muscle
from app.models.exercise import Exercise

import sqlite3
from datetime import date


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
        # self.muscles = muscles
        # self.set_program()
        # save user
        self.update_user_data()

    def __str__(self):
        return "user_id: " + str(self.id) + "\n" + \
               "user_name: " + self.name + "\n" + \
               "height: " + str(self.height) + "\n" + \
               "weight: " + str(self.weight) + "\n" + \
               "bmi: " + str(self.bmi) + "\n"

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        self.update_user_data()

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
        self.update_user_data()

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
        self.update_user_data()

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height
        self.update_user_data()

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight
        self.update_user_data()

    def get_bmi(self):
        return self.bmi

    def set_bmi(self):
        self.bmi = self.weight / ((self.height / 100) ** 2)
        self.update_user_data()

    def get_muscle_by_name(self, muscle_name):
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Muscle WHERE user_id = ? AND name = ?", (self.id, muscle_name))
        muscle_data = c.fetchone()
        if muscle_data is None:
            return None
        conn.close()
        return muscle_data

    def get_all_muscles(self):
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Muscle WHERE user_id = ?", (self.id,))
        muscles_data = c.fetchall()
        if muscles_data is None:
            return None
        conn.close()
        return muscles_data

    def update_muscle(self, muscle_name, points, workout_date=date.today()):
        for cur_muscle in self.muscles:
            if cur_muscle.get_name() == muscle_name:
                cur_muscle.update_points(points, workout_date)
                return True
        return False

    # def set_program(user_id=duration=60, exercises_list=None):
    #     TrainingProgramController.create_program(user_id=self.id, duration=duration, exercises=exercises_list)

    def save_new_user_data(self):
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        c = conn.cursor()
        c.execute("""INSERT INTO Users (id, name, email, password, height, weight, bmi)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""",
                  (self.id, self.name, self.email, self.password, self.height, self.weight, self.bmi))
        conn.commit()
        conn.close()

    def update_user_data(self):
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        c = conn.cursor()
        c.execute("""UPDATE Users SET name = ?, email = ?, password = ?, height = ?,
         weight = ?, bmi = ? WHERE id = ?""",
                  (self.name, self.email, self.password, self.height, self.weight, self.bmi, self.id))
        conn.commit()

    def print_val(self):
        for cur_muscle in self.muscles:
            print(cur_muscle)


if __name__ == '__main__':
    # check connection to database
    conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM Users""")
    print(c.fetchall())
    conn.close()


