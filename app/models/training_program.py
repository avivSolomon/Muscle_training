import sqlite3
from app.database.database import DB_PATH


class TrainingProgram:

    def __init__(self, program_id, user_id, name, day_of_training, duration):
        self.id = program_id
        self.user_id = user_id
        self.day_of_training = day_of_training
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"Training Program: {self.name}\nDay Of Training: {self.day_of_training}\n" \
               f"Duration: {self.duration} days"

    def get_name(self):
        return self.name

    def get_day_of_training(self):
        return self.day_of_training

    def set_day_of_training(self, day_of_training):
        self.day_of_training = day_of_training
        self.update_program_data()

    def get_duration(self):
        return self.duration

    def update_program_data(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("UPDATE TrainingProgram SET day_of_training = ? WHERE id = ?", (self.day_of_training, self.id))
        conn.commit()
        conn.close()

    def save_new_program_data(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO TrainingProgram (user_id, name, day_of_training, duration) VALUES (?, ?, ?, ?)",
                  (self.user_id, self.name, self.day_of_training, self.duration))
        conn.commit()
        conn.close()



