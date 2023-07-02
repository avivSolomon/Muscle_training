

from app.models.training_program import TrainingProgram
from app.models.exercises import Exercise


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

    def create_program(self, name='new_program', duration=60, exercises: list[str] = None):
        if exercises is None:
            init_exercises = [Exercise(name) for name in self.exercises_list]
        else:
            init_exercises = [Exercise(name) for name in exercises]
        return TrainingProgram(name, duration, init_exercises)

    standard_program_list = [create_program(name=key, exercises=val) for key, val in
                             exercises_dict.items()]

    def create_exercise(self, name, sets, repetitions, intensity, muscle):
        exe = Exercise(name, sets, repetitions, intensity)
        self.exercises_dict[muscle].append(exe)

    def get_exercise_by_name(self, name):
        for exercise in self.cur_program:
            if exercise.get_name() == name:
                return exercise
        return None

# Additional code for training program controller functionality


if __name__ == "__main__":
    training_program_controller = TrainingProgramController()

