from app.models.user import User
from app.models.muscle import Muscle
from app.controller.training_program_controller import TrainingProgramController
from app.database.create_database import DB_PATH

import sqlite3


class UserController:
    muscle_list = ['cardiopulmonary_endurance', 'chest', 'back',
                   'shoulders', 'biceps', 'triceps', 'quadriceps',
                   'hamstrings', 'calves', 'abdominal']

    def __init__(self):
        # self.load_data()
        self.current_user = None
        self.current_user_details = None



    @staticmethod
    def get_new_user_id():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT MAX(id) FROM Users")
        max_id = cur.fetchone()[0]
        conn.close()
        return max_id + 1 if max_id is not None else 1

    def create_user(self, name, email, password, height, weight):
        """
        Creates a new user with the provided information.

        Parameters:
        - name (str): Name of the user.
        - email (str): Email of the user.
        - password (str): Password of the user.
        - height (int): Height of the user in centimeters.
        - weight (int): Weight of the user in kilograms.

        Returns:
        - new_user (User): The created User instance.
        """
        user_id = self.get_new_user_id()
        muscles = [Muscle(user_id, name) for name in Muscle.muscle_list]
        TrainingProgramController.create_program(user_id=user_id)
        new_user = User(user_id, name, email, password, height, weight)
        new_user.save_new_user_data()


    @staticmethod
    def get_user_by_email(email):
        """
        Retrieves a user from the database based on the provided email.

        Parameters:
        - email (str): Email of the user.

        Returns:
        - user (list or None): User details as a list [id, name, email, password, height, weight],
                              or None if the user is not found.
        """
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE email = ?", (email,))
        user = cursor.fetchone()
        if user is None:
            return None
        else:
            return [user[0], user[1], user[2], user[3], user[4], user[5]]

    def authenticate_user(self, email, password):
        """
        Authenticates a user against the stored credentials.

        Parameters:
        - email (str): Email of the user.
        - password (str): Password of the user.

        Returns:
        - authenticated (bool): True if the authentication is successful, False otherwise.
        """
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
        """
        Loads the current user based on the current user details.
        """
        self.current_user = User(self.current_user_details[0], self.current_user_details[1],
                                 self.current_user_details[2], self.current_user_details[3],
                                 self.current_user_details[4], self.current_user_details[5])

    def get_current_user(self):
        return self.current_user

    def update_profile(self, new_name=None, new_email=None, new_password=None, new_height=None, new_weight=None):
        """
        Updates the user's profile with the provided information.

        Parameters:
        - new_name (str): New name of the user (optional).
        - new_email (str): New email of the user (optional).
        - new_password (str): New password of the user (optional).
        - new_height (float): New height of the user in centimeters (optional).
        - new_weight (float): New weight of the user in kilograms (optional).
        """
        # Update the user's details in the database
        # Implement the update logic here
        user = self.get_current_user()
        user.set_name(new_name) if new_name != '' else user.get_name()
        user.set_email(new_email) if new_email != '' else user.get_email()
        user.set_password(new_password) if new_password != '' else user.get_password()
        user.set_height(int(new_height)) if new_height != '' else user.get_height()
        user.set_weight(int(new_weight)) if new_weight != '' else user.get_weight()
        user.set_bmi()
        user.update_user_data()


