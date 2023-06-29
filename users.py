from muscle import Muscle
import data_base
import sqlite3
from datetime import date

class User:
    muscle_list = ['cardiopulmonary_endurance', 'chest', 'back',
                   'shoulders', 'biceps', 'triceps', 'quadriceps',
                   'hamstrings', 'calves', 'abdominal']

    def __init__(self, user_id, username, height=1.75, weight=70):
        self.user_id = user_id
        self.user_name = username
        self.height = height
        self.weight = weight
        self.bmi = self.weight / (self.height ** 2)
        self.muscles = [Muscle(name) for name in User.muscle_list]

    def __str__(self):
        return "user_id: " + str(self.user_id) + "\n" + \
               "user_name: " + self.user_name + "\n" + \
               "height: " + str(self.height) + "\n" + \
               "weight: " + str(self.weight) + "\n" + \
               "muscles: " + str(self.muscles)

    def get_id(self):
        return self.user_id

    def get_name(self):
        return self.user_name

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_muscle(self, muscle_name):
        for cur_muscle in self.muscles:
            if cur_muscle.get_name() == muscle_name:
                return cur_muscle
        return None

    def get_muscle_list(self):
        return self.muscles

    def update_muscle(self, muscle_name, points, date=date.today()):
        for cur_muscle in self.muscles:
            if cur_muscle.get_name() == muscle_name:
                cur_muscle.update_points(points, date)
                return True
        return False

    def update_height(self, height):
        self.height = height

    def update_weight(self, weight):
        self.weight = weight

    def update_name(self, name):
        self.user_name = name

    def save_data(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE user_id=?", (self.user_id,))
        c.execute("DELETE FROM muscles WHERE user_id=?", (self.user_id,))
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                  (self.user_id, self.user_name, self.height, self.weight))
        for cur_muscle in self.muscles:
            c.execute("INSERT INTO muscles VALUES (?, ?, ?, ?, ?)",
                      (self.user_id,
                       cur_muscle.get_name(),
                       cur_muscle.get_points(),
                       cur_muscle.get_workout_date(),
                       cur_muscle.get_rest_time()))
        conn.commit()
        conn.close()

    def print_val(self):
        for cur_muscle in self.muscles:
            print(f'muscle name: {cur_muscle.get_name()}\n\t point: {cur_muscle.get_points()}, recent trained at: {cur_muscle.get_workout_date()}, restin time left: {cur_muscle.get_rest_time()}')


