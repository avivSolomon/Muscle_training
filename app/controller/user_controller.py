from app.models.user import User
from app.models.muscle import Muscle
# from app.controller.training_program_controller import TrainingProgramController

import sqlite3
from datetime import datetime
import sqlite3


class UserController:
    muscle_list = ['cardiopulmonary_endurance', 'chest', 'back',
                   'shoulders', 'biceps', 'triceps', 'quadriceps',
                   'hamstrings', 'calves', 'abdominal']

    def __init__(self):
        # self.load_data()
        self.current_user = None
        self.current_user_details = None

    def is_valid_email(self, email):
        # Implement email validation logic
        return "@" in email

    @staticmethod
    def get_new_user_id():
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        cur = conn.cursor()
        cur.execute("SELECT MAX(id) FROM Users")
        max_id = cur.fetchone()[0]
        conn.close()
        return max_id + 1 if max_id is not None else 1

    def create_user(self, name, email, password, height, weight):
        user_id = self.get_new_user_id()
        muscles = [Muscle(user_id, name) for name in Muscle.muscle_list]
        program = None
        new_user = User(user_id, name, email, password, height, weight, muscles, program)
        new_user.save_new_user_data()

    @staticmethod
    def get_user_by_email(email):
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE email = ?", (email,))
        user = cursor.fetchone()
        if user is None:
            return None
        else:
            return [user[0], user[1], user[2], user[3], user[4], user[5]]

    def authenticate_user(self, email, password):
        # Authenticate user against stored credentials
        # Implement the authentication logic here
        self.current_user_details = self.get_user_by_email(email)
        if self.current_user_details is None:
            return False
        if self.current_user_details[3] != password:
            return False
        self.load_user()
        return True

    def load_user(self):
        self.current_user = User(self.current_user_details[0], self.current_user_details[1],
                                 self.current_user_details[2], self.current_user_details[3],
                                 self.current_user_details[4], self.current_user_details[5])

    def get_current_user(self):
        return self.current_user

    def update_profile(self, new_name=None, new_email=None, new_password=None):
        # Update the user's details in the database
        # Implement the update logic here
        user = self.get_current_user()
        user.set_name(new_name) if new_name is not None else user.get_name()
        user.set_email(new_email) if new_email is not None else user.get_email()
        user.set_password(new_password) if new_password is not None else user.get_password()


