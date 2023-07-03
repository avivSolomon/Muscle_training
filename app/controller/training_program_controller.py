import sqlite3
from app.models.training_program import TrainingProgram
from app.models.exercise import Exercise
from app.models.muscle import Muscle


class TrainingProgramController:
    exercises_dict = {'quadriceps': ['squats', 'lunges', 'leg_press'],
                      'hamstring': ['deadlifts', 'hamstring_curls'],
                      'back': ['pull_ups', 'rows', 'lat_pull_downs', 'planks'],
                      'biceps': ['bicep_curls', 'hammer_curls'],
                      'chest': ['bench_press', 'push_ups', 'chest_flies', 'dumbbell_press'],
                      'shoulders': ['shoulder_press', 'lateral_raises', 'front_raises'],
                      'triceps': ['triceps_dips', 'triceps_push_downs'],
                      'abdominal': ['planks', 'sit_ups', 'russian_twists'],
                      'cardiopulmonary_endurance': ['running', 'cycling', 'swimming']}

    exercises_list = list(exercises_dict.values())

    def __init__(self):
        self.cur_program = None

    @staticmethod
    def standard_program_list():
        a = ['squats', 'lunges', 'leg_press', 'deadlifts', 'hamstring_curls', 'calf_raises',
             'pull_ups', 'rows', 'lat_pulldowns', 'bicep_curls', 'hammer_curls']
        b = ['bench_press', 'push_ups', 'chest_flies', 'dumbbell_press', 'shoulder_press',
             'lateral_raises', 'front_raises', 'triceps_dips', 'triceps_pushdowns', 'planks',
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
        program = []
        if exercises is None:
            exercises = TrainingProgramController.standard_program_list()
        for day_of_training in range(1, duration+1):
            daily_workout = exercises[day_of_training % len(exercises)]
            daily_program = []
            for name in daily_workout:
                key = TrainingProgramController.get_key_value(TrainingProgramController.exercises_dict,name)
                if key is not None:
                    intensity = min([intensity_dict[k] for k in key])
                else:
                    intensity = 1
                daily_program.append(Exercise(program_id, day_of_training, name, intensity=intensity))
            program.append(daily_program)

        TrainingProgram(program_id, user_id, program_name, day_of_training=1, duration=duration)



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
        conn = sqlite3.connect(r'C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db')
        c = conn.cursor()
        c.execute("SELECT MAX(id) FROM TrainingProgram")
        max_id = c.fetchone()[0]
        conn.close()
        return max_id + 1 if max_id is not None else 1

# Additional code for training program controller functionality


if __name__ == "__main__":
    training_program_controller = TrainingProgramController()

