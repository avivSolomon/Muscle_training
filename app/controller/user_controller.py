from app.models.user import User
from app.models.muscle import Muscle
from app.controller.training_program_controller import TrainingProgramController

import sqlite3
from datetime import datetime


class UserController:
    muscle_list = ['cardiopulmonary_endurance', 'chest', 'back',
                   'shoulders', 'biceps', 'triceps', 'quadriceps',
                   'hamstrings', 'calves', 'abdominal']

    def __init__(self):
        # self.load_data()
        self.current_user = None

    def is_valid_email(self, email):
        # Implement email validation logic
        return "@" in email

    def create_user(self, name, email, password, height, weight):
        # Create a new User instance
        user_id = ...
        # new_user_id = len(self.users)
        muscles = [Muscle(name) for name in self.muscle_list]
        program = TrainingProgramController.get_program_list()[-1]

        new_user = User(user_id, name, email, password, height, weight, muscles, program)
        self.users.append(new_user)
        # update data.db
        self.save_user(new_user)

    def save_user(self, user):
        # Store user details in the database
        # Implement the database storage logic here
        pass

    # def save_data(self):
    #     """update data.db from self.users"""
    #     conn = sqlite3.connect('data.db')
    #     c = conn.cursor()
    #     c.execute("DELETE FROM users")
    #     c.execute("DELETE FROM muscles")
    #     for cur_user in self.users:
    #         c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
    #                   (cur_user.get_id(), cur_user.get_name(), cur_user.get_height(), cur_user.get_weight()))
    #         for cur_muscle in cur_user.get_muscle_list():
    #             c.execute("INSERT INTO muscles VALUES (?, ?, ?, ?, ?)",
    #                       (cur_user.get_id(),
    #                        cur_muscle.get_name(),
    #                        cur_muscle.get_points(),
    #                        cur_muscle.get_workout_date(),
    #                        cur_muscle.get_rest_time()))
    #     conn.commit()
    #     conn.close()

    def authenticate_user(self, email, password):
        # Authenticate user against stored credentials
        # Implement the authentication logic here
        self.current_user = ...
        return True

    # def get_user(self, user_id):
    #     for cur_user in self.users:
    #         if cur_user.get_id() == user_id:
    #             return cur_user
    #     return None

    def get_current_user(self):
        return self.current_user

    def update_profile(self, new_name=None, new_email=None, new_password=None):
        # Update the user's details in the database
        # Implement the update logic here
        user = self.get_current_user()
        user.set_name(new_name) if new_name is not None else user.get_name()
        user.set_email(new_email) if new_email is not None else user.get_email()
        user.set_password(new_password) if new_password is not None else user.get_password()

    # def update_user(self, user_id, user_name, height, weight):
    #     cur_user = self.get_user(user_id)
    #     if cur_user is None:
    #         return False
    #     cur_user.update_name(user_name)
    #     cur_user.update_height(height)
    #     cur_user.update_weight(weight)
    #     # update data.db
    #     cur_user.save_data()
    #     return True


    def get_user_list(self):
        return self.users

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
            cur_muscle.update_points(row[2], datetime.strptime(row[3], date_format).date())
        conn.close()


