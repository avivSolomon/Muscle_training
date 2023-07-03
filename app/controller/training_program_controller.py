import sqlite3
from app.models.training_program import TrainingProgram
from app.models.exercise import Exercise


class TrainingProgramController:
    exercises_dict = {'Quadriceps': ['squats', 'lunges', 'leg_press'],
                      'hamstring': ['deadlifts', 'hamstring_curls'],
                      'Back': ['pull_ups', 'rows', 'lat_pull_downs', 'planks'],
                      'Biceps': ['bicep_curls', 'hammer_curls'],
                      'Chest': ['bench_press', 'push_ups', 'chest_flies', 'dumbbell_press'],
                      'Shoulders': ['shoulder_press', 'lateral_raises', 'front_raises'],
                      'Triceps': ['triceps_dips', 'triceps_push_downs'],
                      'Abdominal': ['planks', 'sit_ups', 'russian_twists'],
                      'cardiopulmonary_endurance': ['running', 'cycling', 'swimming']}

    exercises_list = list(exercises_dict.values())

    def __init__(self):
        self.cur_program = None

    def create_program(self, user_id, name='new_program', duration=60, exercises: list[list[str]] = None):
        program_id = self.get_new_program_id()
        program = []
        if exercises is None:
            for day_of_training in range(1, duration+1):
                daily_workout = self.standard_program_list()[day_of_training % 2]
                program.append(
                    [Exercise(program_id, day_of_training, name) for name in daily_workout])
        # else:

        #     init_exercises = [Exercise(program_id, day_of_training, name) for name in exercises]

        TrainingProgram(program_id, user_id, name, day_of_training=1, duration=duration)

    @staticmethod
    def standard_program_list():
        a = ['squats', 'lunges', 'leg_press', 'deadlifts', 'hamstring_curls', 'calf_raises',
             'pull_ups', 'rows', 'lat_pulldowns', 'bicep_curls', 'hammer_curls']

        b = ['bench_press', 'push_ups', 'chest_flies', 'dumbbell_press', 'shoulder_press',
             'lateral_raises','front_raises', 'triceps_dips', 'triceps_pushdowns', 'planks',
             'sit_ups', 'russian_twists']

        standard = [a,b]
        return standard

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

