from datetime import date, timedelta
import sqlite3
from app.database.create_database import DB_PATH


class Muscle:
    muscle_list = ['cardiopulmonary_endurance', 'chest', 'back',
                   'shoulders', 'biceps', 'triceps', 'quadriceps',
                   'hamstrings', 'calves', 'abdominal']

    def __init__(self, user_id, name, points=0, workout_date=date(1970, 1, 1),
                 rest_time=date(1970, 1, 1)):
        self.user_id = user_id
        self.name = name
        self.points = points
        self.workout_date = workout_date
        self.rest_time = rest_time
        self.save_new_muscle_data()

    def __str__(self):
        return "name: " + self.name + "\n" + \
               "points: " + str(self.points) + "\n" + \
               "date: " + str(self.workout_date) + "\n" + \
               "rest_time: " + str(self.rest_time)

    def get_name(self):
        return self.name

    @staticmethod
    def get_muscles_by_user_id(user_id):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM Muscle WHERE user_id=?", (user_id,))
        muscles = c.fetchall()
        conn.close()
        return muscles

    @staticmethod
    def get_all_the_muscles_points(user_id):
        dict_muscle_points = {}
        for muscle in Muscle.get_muscles_by_user_id(user_id):
            dict_muscle_points[muscle[1]] = muscle[2]
        return dict_muscle_points

    def get_points(self):
        return self.points

    def get_workout_date(self):
        return self.workout_date

    def get_rest_time(self):
        return self.rest_time

    @staticmethod
    def calculate_rest_time(points):
        day_rest = 0 if points < 2 else 1 if points < 3 else 2
        return date.today() + timedelta(days=day_rest)

    def update_points(self, points, workout_date=date.today()):
        self.points = points
        self.workout_date = workout_date
        day_rest = 0 if points<2 else 1 if points<3 else 2
        self.rest_time = self.workout_date + timedelta(days=day_rest)
        self.update_muscle_data()

    def in_rest(self):
        return (self.rest_time - date.today()).days > 0

    def get_muscle_value(self):
        return [self.points, self.workout_date, self.rest_time]

    def save_new_muscle_data(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO Muscle (user_id, name, points, workout_date, rest_time) VALUES (?, ?, ?, ?, ?)",
                  (self.user_id, self.name, self.points, self.workout_date, self.rest_time))
        conn.commit()
        conn.close()

    def update_muscle_data(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("UPDATE Muscle SET points=?, workout_date=?, rest_time=? WHERE user_id=? AND name=?",
                  (self.points, self.workout_date, self.rest_time, self.user_id, self.name))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM Muscle where user_id=1")
    print(c.fetchall())
    conn.close()
    # while True:
    #     today = date.today()
    #     time.sleep(24*60*60)