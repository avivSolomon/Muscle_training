import sqlite3
from datetime import date

class User:
    def __init__(self, user_id, name, email, password, height, weight, muscles, program):
        # Login Information
        self.user_id = user_id
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

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        # self.save_data()

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_id(self):
        return self.user_id

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_bmi(self):
        return self.bmi

    def set_height(self, height):
        self.height = height
        # self.save_data()

    def set_weight(self, weight):
        self.weight = weight
        # self.save_data()

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
                # update data.db
                self.save_data()
                return True
        return False

    def get_program(self):
        return self.program

    def set_program(self, program=None):
        if program is None:
            program =  if self.bmi > 30 else ...
        self.program = program


    def workout(self, exercise):
        pass


    def save_data(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE user_id=?", (self.user_id,))
        c.execute("DELETE FROM muscles WHERE user_id=?", (self.user_id,))
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                  (self.user_id, self.name, self.height, self.weight))
        for cur_muscle in self.muscles:
            c.execute("INSERT INTO muscles VALUES (?, ?, ?, ?, ?)",
                      (self.user_id,
                       cur_muscle.get_name(),
                       cur_muscle.get_points(),
                       cur_muscle.get_workout_date(),
                       cur_muscle.get_rest_time()))
        conn.commit()
        conn.close()

    def __str__(self):
        return "user_id: " + str(self.user_id) + "\n" + \
               "user_name: " + self.name + "\n" + \
               "height: " + str(self.height) + "\n" + \
               "weight: " + str(self.weight) + "\n" + \
                "bmi: " + str(self.bmi) + "\n" + \
               "muscles: " + str(self.muscles)

    def print_val(self):
        for cur_muscle in self.muscles:
            print(cur_muscle)

