import sqlite3
from app.models.training_program import TrainingProgram
from app.models.exercise import Exercise
from app.models.muscle import Muscle
from datetime import date
from app.database.create_database import DB_PATH


class TrainingProgramController:
    exercises_dict = {'quadriceps': ['squats', 'lunges', 'leg_press'],
                      'hamstrings': ['deadlifts', 'hamstring_curls', 'calf_raises'],
                      'back': ['pull_ups', 'rows', 'lat_pull_downs', 'planks'],
                      'biceps': ['bicep_curls', 'hammer_curls'],
                      'chest': ['bench_press', 'push_ups', 'chest_flies', 'dumbbell_press'],
                      'shoulders': ['shoulder_press', 'lateral_raises', 'front_raises'],
                      'triceps': ['triceps_dips', 'triceps_push_downs'],
                      'abdominal': ['planks', 'sit_ups', 'russian_twists'],
                      'cardiopulmonary_endurance': ['running', 'cycling', 'swimming'],
                      'calves': ['calf_raises', 'jumping_jacks']}

    exercises_list = list(exercises_dict.values())

    def __init__(self, user_id):
        self.user_id = user_id
        self.user_program = self.load_recent_program()
        self.program_day_of_training = self.user_program.get_day_of_training()

    def load_recent_program(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM TrainingProgram WHERE user_id=?", (self.user_id,))
        program_data = c.fetchone()
        conn.close()
        if program_data is None:
            return None
        program_id, user_id, name, day_of_training, duration = program_data
        return TrainingProgram(program_id, user_id, name, day_of_training, duration)

    def get_user_program(self):
        return self.user_program

    def get_today_exercises(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM Exercise WHERE training_program_id=? AND day_of_training=?",
                  (self.user_program.id, self.user_program.day_of_training))
        exercises_data = c.fetchall()
        conn.close()
        return exercises_data

    def workout(self):
        # get exercise_id, name, points from exercise table for each exercise in daily_workout
        # update points for each muscle in muscles table
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        c = conn.cursor()
        c.execute("""SELECT Exercise.id, Exercise.value_points,
                            Exercise.name, Exercise.intensity,
                            Exercise.sets, Exercise.reps
                            FROM Exercise
                            JOIN TrainingProgram ON TrainingProgram.day_of_training = Exercise.day_of_training
                            WHERE TrainingProgram.user_id = ?""", (self.user_id,))
        daily_workout = c.fetchall()
        # print(daily_workout)
        for exercise in daily_workout:
            print(f"exercise name: {exercise[2]}\n exercise intensity: {exercise[3]}\n exercise sets: {exercise[4]}\n "
                  f"exercise reps: {exercise[5]}\n")
        change_list = list(input(""" If there are exercises that did not perform as planned, 
                                    \nwrite down the names of the exercises here 
                                    \nSeparate with the help of "," between drill and drill if there are:""").split(
            ","))
        user_muscles = Muscle.get_muscles_by_user_id(self.user_id)
        for exercise in daily_workout:
            if exercise[2] in change_list:
                Exercise.update_exe_details(exercise[0])
            exe_id, points, exe_name = exercise[0], exercise[1], exercise[2]
            for muscle in user_muscles:
                if exe_name in TrainingProgramController.exercises_dict[muscle[1]]:
                    muscle_id = muscle[0]
                    update_points = muscle[2] + points
                    workout_date = date.today()
                    rest_date = Muscle.calculate_rest_time(points)
                    c.execute("""UPDATE Muscle SET points = ?, workout_date = ?, rest_time = ?
                                WHERE user_id = ?""",
                              (update_points, workout_date, rest_date, muscle_id))
                    c.execute("""INSERT INTO ExerciseHistory (user_id, exercise_id, workout_date)
                                VALUES (?, ?, ?)""",
                              (self.user_id, exe_id, workout_date))
                    conn.commit()
        conn.close()
        self.user_program.set_day_of_training(self.program_day_of_training + 1)

    @staticmethod
    def standard_program_list():
        a = ['squats', 'lunges', 'leg_press', 'deadlifts', 'hamstring_curls', 'calf_raises',
             'pull_ups', 'rows', 'lat_pull_downs', 'bicep_curls', 'hammer_curls']
        b = ['bench_press', 'push_ups', 'chest_flies', 'dumbbell_press', 'shoulder_press',
             'lateral_raises', 'front_raises', 'triceps_dips', 'triceps_push_downs', 'planks',
             'sit_ups', 'russian_twists']
        return [a, b]

    @staticmethod
    def intensity_level(user_id):
        muscle_intensity_level_dict = Muscle.get_all_the_muscles_points(user_id)
        for muscle in muscle_intensity_level_dict.keys():
            muscle_intensity_level_dict[muscle] = len(str(int(muscle_intensity_level_dict[muscle])))
        return muscle_intensity_level_dict

    @staticmethod
    def get_key_value(exe_dict, value):
        key_list = []
        for k, v in exe_dict.items():
            if value in v:
                key_list.append(k)
        return key_list

    @staticmethod
    def create_program(user_id, program_name='new_program', duration=60,
                       exercises: list[list[str]] = None):
        program_id = TrainingProgramController.get_new_program_id()
        intensity_dict = TrainingProgramController.intensity_level(user_id)
        if exercises is None:
            exercises = TrainingProgramController.standard_program_list()
        for day_of_training in range(1, duration + 1):
            daily_workout = exercises[day_of_training % len(exercises)]
            for name in daily_workout:
                key = TrainingProgramController.get_key_value(TrainingProgramController.exercises_dict, name)
                intensity = min([intensity_dict[k] for k in key]) if key is not None else 1
                Exercise(program_id, day_of_training, name, intensity)
        training_program = TrainingProgram(program_id, user_id, program_name, day_of_training=1, duration=duration)
        training_program.save_new_program_data()

    @staticmethod
    def new_training(user_id, duration, day_of_training):
        need_new_program = (duration == day_of_training)
        if need_new_program:
            TrainingProgramController.create_program(user_id)

    # def create_exercise(self, name, sets, repetitions, intensity, muscle):
    #     exe = Exercise(name, sets, repetitions, intensity)
    #     self.exercises_dict[muscle].append(exe)

    def get_exercise_by_name(self, name):
        for exercise in self.cur_program:
            if exercise.get_name() == name:
                return exercise
        return None

    @staticmethod
    def get_new_program_id():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT MAX(id) FROM TrainingProgram")
        max_id = c.fetchone()[0]
        conn.close()
        return max_id + 1 if max_id is not None else 1


# Additional code for training program controller functionality


if __name__ == "__main__":
    pass

