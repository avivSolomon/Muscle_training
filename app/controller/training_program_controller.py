from poetry.console.commands import self

from app.models.training_program import TrainingProgram
from app.models.exercises import Exercise

class TrainingProgramController:
    def __init__(self):
        self.cur_program = None
        self.exercises_dict = {'Quadriceps': ['squats', 'lunges', 'leg_press', 'deadlifts',
                                              'hamstring_curls', 'calf_raises'],
                               'Back': ['pull_ups', 'rows', 'lat_pull_downs', 'planks'],
                               'Biceps': ['bicep_curls', 'hammer_curls'],
                               'Chest': ['bench_press', 'push_ups', 'chest_flies', 'dumbbell_press'],
                               'Shoulders': ['shoulder_press', 'lateral_raises', 'front_raises'],
                               'Triceps': ['triceps_dips', 'triceps_push_downs'],
                               'Abdominal': ['planks', 'sit_ups', 'russian_twists'],
                               'cardiopulmonary_endurance': ['running', 'cycling', 'swimming']}
        self.exercises_list = list(self.exercises_dict.values())
        self.program_list = [self.create_program(name=key, exercises=val) for key, val in self.exercises_dict.items()]

    def create_program(self, name='new_user', duration=60, exercises=None):
        if exercises is None:
            exercises = [Exercise(name) for name in self.exercises_list]
        return TrainingProgram(name, duration, exercises)

    def add_exercise_to_program(self, program, exercise):
        pass

    def create_exercise(self, name, duration, intensity):
        exe = Exercise(name, duration, intensity)
        self.exercises_list += exe

    def get_program_list(self):
        return self.program_list
    def get_exercise_by_name(self, name):
        for exercise in self.cur_program:
            if exercise.get_name() == name:
                return exercise
        return None

# Additional code for training program controller functionality

if __name__ == "__main__":
    training_program_controller = TrainingProgramController()

