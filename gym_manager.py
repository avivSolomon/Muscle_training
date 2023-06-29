import sqlite3
from users import User
from datetime import datetime


class GymManager:
    def __init__(self):
        self.load_data()

    def create_user(self, user_name, height, weight):
        new_user_id = len(self.users)
        new_user = User(new_user_id, user_name, height, weight)
        self.users.append(new_user)
        # update data.db
        new_user.save_data()

    def get_user(self, user_id):
        for cur_user in self.users:
            if cur_user.get_id() == user_id:
                return cur_user
        return None

    def get_user_list(self):
        return self.users

    def update_user(self, user_id, user_name, height, weight):
        cur_user = self.get_user(user_id)
        if cur_user is None:
            return False
        cur_user.update_name(user_name)
        cur_user.update_height(height)
        cur_user.update_weight(weight)
        # update data.db
        cur_user.save_data()
        return True

    def load_data(self):
        """load data from data.db and save it to self.users"""
        self.users = []
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        # load users
        c.execute("SELECT * FROM users")
        for row in c.fetchall():
            new_user = User(row[0], row[1], row[2], row[3])
            self.users.append(new_user)
        # load muscles
        c.execute("SELECT * FROM muscles")
        date_format = "%Y-%m-%d"
        for row in c.fetchall():
            cur_user = self.get_user(row[0])
            if cur_user is None:
                continue
            cur_muscle = cur_user.get_muscle(row[1])
            if cur_muscle is None:
                continue
            cur_muscle.update_points(row[2], datetime.strptime(row[3], date_format))
        conn.close()

    def save_data(self):
        """update data.db from self.users"""
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("DELETE FROM users")
        c.execute("DELETE FROM muscles")
        for cur_user in self.users:
            c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                      (cur_user.get_id(), cur_user.get_name(), cur_user.get_height(), cur_user.get_weight()))
            for cur_muscle in cur_user.get_muscle_list():
                c.execute("INSERT INTO muscles VALUES (?, ?, ?, ?, ?)",
                          (cur_user.get_id(),
                           cur_muscle.get_name(),
                           cur_muscle.get_points(),
                           cur_muscle.get_workout_date(),
                           cur_muscle.get_rest_time()))
        conn.commit()
        conn.close()