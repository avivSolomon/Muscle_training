import sqlite3
from app.models.training_program import TrainingProgram
from app.models.exercise import Exercise
from app.models.muscle import Muscle
from datetime import date
from app.database.create_database import DB_PATH


class TrainingProgramController:
    """
    Controller class for managing training programs.

    Attributes:
    - exercises_dict (dict): Dictionary mapping muscle names to a list of exercises targeting that muscle.
    - exercises_list (list): List of lists containing all exercises in the program.

    Methods:
    - __init__(user_id): Initializes a TrainingProgramController instance for a specific user.
    - load_recent_program(): Loads the most recent training program for the user.
    - get_user_program(): Retrieves the user's current training program.
    - get_today_exercises(): Retrieves the exercises scheduled for the current day of the user's program.
    - workout(): Performs the workout routine for the current day, updating muscle points and exercise history.
    - standard_program_list(): Returns a list of standard exercise programs.
    - intensity_level(user_id): Calculates the intensity level of each muscle for a given user.
    - get_key_value(exe_dict, value): Retrieves the keys from a dictionary based on a specific value.
    - create_program(user_id, program_name='new_program', duration=60, exercises=None): Creates a new training program.
    - new_training(user_id, duration, day_of_training): Checks if a new training program is needed and creates one if necessary.
    - get_new_program_id(): Generates a new program ID.
    """

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
        """
        Loads the most recent training program for the user.

        Returns:
        - user_program (TrainingProgram or None): The most recent TrainingProgram instance
                                                    for the user,or None if no program is found.
        """
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM TrainingProgram WHERE user_id=? AND id = (SELECT MAX(id) FROM TrainingProgram)", (self.user_id,))
        program_data = c.fetchone()
        conn.close()
        if program_data is None:
            return None
        program_id, user_id, name, day_of_training, duration = program_data
        return TrainingProgram(program_id, user_id, name, day_of_training, duration)

    def get_user_program(self):
        return self.user_program

    def get_today_exercises(self):
        """
        Retrieves the exercises scheduled for the current day of the user's program.

        Returns:
        - exercises_data (list): List of exercises data for the current day of training.
        """
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM Exercise WHERE training_program_id=? AND day_of_training=?",
                  (self.user_program.id, self.user_program.day_of_training))
        exercises_data = c.fetchall()
        conn.close()
        return exercises_data

    def workout(self):
        """
        Performs the workout routine for the current day,
         updating the program training day, muscle points and exercise history.
        """
        # get the data of today (the workout date)
        workout_date = date.today()
        # get all the muscles details of the user by the user id ->list[list]
        user_muscles = Muscle.get_muscles_by_user_id(self.user_id)
        # get all the exercises for the current day
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""SELECT Exercise.id, Exercise.value_points,
                            Exercise.name, Exercise.intensity,
                            Exercise.sets, Exercise.reps
                            FROM Exercise
                            JOIN TrainingProgram ON TrainingProgram.day_of_training = Exercise.day_of_training
                            WHERE TrainingProgram.user_id = ?""", (self.user_id,))
        daily_workout = c.fetchall()
        # for each exercise in daily_workout, ask the user if we need to update the exercise
        # if yes then update the exercise
        for exercise in daily_workout:
            points = exercise[1]
            print(f"exercise name: {exercise[2]}\n exercise intensity: {exercise[3]}\n exercise sets: {exercise[4]}\n "
                  f"exercise reps: {exercise[5]}\n")
            while True:
                change = input(f"Was the exercise {exercise[2]} carried out as planned?"
                               f" (Yes or No):").lower()
                if change in ('yes', 'no', ""):
                    if change == 'no':
                        points = Exercise.update_exe_details(exercise[0])
                    break
                else:
                    print('\nPlease enter a valid input (yes or no) to continue\n')
            exe_id, exe_name = exercise[0], exercise[2]
            # save the exercise to the exercise history
            c.execute("""INSERT INTO ExerciseHistory (user_id, exercise_id, workout_date)
                                    VALUES (?, ?, ?)""",
                      (self.user_id, exe_id, workout_date))
            conn.commit()
            # update points, workout_date and ret_time for each muscle in muscles table
            for muscle in user_muscles:
                if exe_name in TrainingProgramController.exercises_dict[muscle[1]]:
                    muscle_id = muscle[0]
                    update_points = muscle[2] + points
                    rest_date = Muscle.calculate_rest_time(points)
                    c.execute("""UPDATE Muscle SET points = ?, workout_date = ?, rest_time = ?
                                WHERE user_id = ?""",
                              (update_points, workout_date, rest_date, muscle_id))
                    conn.commit()
        conn.close()
        # add 1 to the day of training
        self.user_program.set_day_of_training(self.program_day_of_training + 1)

    def get_muscles_status(self):
        muscles_status = Muscle.get_muscles_by_user_id(self.user_id)
        return muscles_status

    @staticmethod
    def standard_program_list():
        """
        Returns a list of standard exercise programs.

        Returns:
        - program_list (list): List of lists containing exercises for each day of the program.
        """
        a = ['squats', 'lunges', 'leg_press', 'deadlifts', 'hamstring_curls', 'calf_raises',
             'pull_ups', 'rows', 'lat_pull_downs', 'bicep_curls', 'hammer_curls']
        b = ['bench_press', 'push_ups', 'chest_flies', 'dumbbell_press', 'shoulder_press',
             'lateral_raises', 'front_raises', 'triceps_dips', 'triceps_push_downs', 'planks',
             'sit_ups', 'russian_twists']
        return [a, b]

    @staticmethod
    def intensity_level(user_id):
        """
        Calculates the intensity level of each muscle for a given user.

        Returns:
        - muscle_intensity_level_dict (dict): Dictionary mapping muscle names to their intensity levels.
        """
        muscle_intensity_level_dict = Muscle.get_all_the_muscles_points(user_id)
        for muscle in muscle_intensity_level_dict.keys():
            muscle_intensity_level_dict[muscle] = len(str(int(muscle_intensity_level_dict[muscle])))
        return muscle_intensity_level_dict

    @staticmethod
    def get_key_value(exe_dict, value):
        """
        Retrieves the keys from a dictionary based on a specific value.

        Parameters:
        - exe_dict (dict): Dictionary to search.
        - value: Value to search for.

        Returns:
        - key_list (list): List of keys associated with the specified value,
        or None.
        """
        key_list = []
        for k, v in exe_dict.items():
            if value in v:
                key_list.append(k)
        return key_list if len(key_list) > 0 else None

    @staticmethod
    def create_program(user_id, program_name='new_program', duration=60,
                       exercises: list[list[str]] = None):
        """
        Creates a new training program.

        Parameters:
        - user_id (int): ID of the user.
        - program_name (str): Name of the program (default: 'new_program').
        - duration (int): Duration of the program in days (default: 60).
        - exercises (list): List of lists containing exercises for each day of the program.
                            If None, the standard program list will be used.

        """
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

    @staticmethod
    def get_new_program_id():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT MAX(id) FROM TrainingProgram")
        max_id = c.fetchone()[0]
        conn.close()
        return max_id + 1 if max_id is not None else 1


if __name__ == "__main__":
    pass
