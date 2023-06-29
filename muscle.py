from datetime import date, timedelta
import sqlite3
import time


class Muscle:
    # while True:
    #     today = date.today()
    #     time.sleep(24*60*60)

    def __init__(self, name, points=0, workout_date=date(1970,1,1), rest_time=date(1970,1,1)):
        self.name = name
        self.points = points
        self.workout_date = workout_date
        self.rest_time = rest_time

    def __str__(self):
        return "name: " + self.name + "\n" + \
               "points: " + str(self.points) + "\n" + \
               "date: " + str(self.workout_date) + "\n" + \
               "rest_time: " + str(self.rest_time)

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def get_workout_date(self):
        return self.workout_date

    def get_rest_time(self):
        return self.rest_time

    def update_points(self, points, workout_date=date.today()):
        self.points = points
        self.workout_date = workout_date
        day_rest = 0 if points<2 else 1 if points<3 else 2
        self.rest_time = self.workout_date + timedelta(days=day_rest)
        self.save_muscle_data()

    def in_rest(self):
        return (self.rest_time - date.today()).days > 0

    def get_muscle_value(self):
        return [self.points, self.workout_date, self.rest_time]

    def save_muscle_data(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("UPDATE muscles SET points=?, workout_date=?, rest_time=? WHERE muscle_name=?",
                  (self.points, self.workout_date, self.rest_time, self.name))
        conn.commit()
        conn.close()

# Retrieve all classes that inherit from BaseClass
subclasses = Muscle.__subclasses__()
# Create instances of each subclass
# muscle_subclasses = [subclass() for subclass in subclasses]
# print(muscle_subclasses)