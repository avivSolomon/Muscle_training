from app.database.database import DB_PATH

import sqlite3


class User:
    """
    Represents a user with login information and body measurements.
    """
    def __init__(self, user_id, name, email, password, height, weight):
        """
        Initializes a User instance.

        Parameters:
        - user_id (int): User ID.
        - name (str): User name.
        - email (str): User email.
        - password (str): User password.
        - height (int): User height in centimeters.
        - weight (int): User weight in kilograms.
        """

        # Login Information
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        # bmi Information
        self.height = height
        self.weight = weight
        self.bmi = self.weight / ((self.height / 100) ** 2)
        # save user
        self.update_user_data()

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
        """
        Retrieves muscle data for the user based on the muscle name.

        Parameters:
        - muscle_name (str): Name of the muscle.

        Returns:
        - muscle_data (tuple): Muscle data if found, or None if not found.
        """
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM Muscle WHERE user_id = ? AND name = ?", (self.id, muscle_name))
        muscle_data = c.fetchone()
        if muscle_data is None:
            return None
        conn.close()
        return muscle_data

    def save_new_user_data(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""INSERT INTO Users (id, name, email, password, height, weight, bmi)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""",
                  (self.id, self.name, self.email, self.password, self.height, self.weight, self.bmi))
        conn.commit()
        conn.close()

    def update_user_data(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""UPDATE Users SET name = ?, email = ?, password = ?, height = ?,
         weight = ?, bmi = ? WHERE id = ?""",
                  (self.name, self.email, self.password, self.height, self.weight, self.bmi, self.id))
        conn.commit()


if __name__ == '__main__':
    # check connection to database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""SELECT * FROM Users""")
    print(c.fetchall())
    conn.close()


