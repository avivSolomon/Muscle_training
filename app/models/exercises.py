from poetry.console.commands import self

from datetime import date


class Exercise:
    def __init__(self, name, intensity: int = 1, sets=3, reps=10):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.intensity = intensity
        self.Value_points = round(sets * intensity * reps / 50)
        self.workout_date = date.today()

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.sets

    def set_duration(self, sets):
        self.sets = sets

    def get_intensity(self):
        return self.intensity

    def set_intensity(self, intensity):
        self.intensity = intensity

    def get_reps(self):
        return self.reps

    def set_reps(self, reps):
        self.reps = reps


# Additional code for exercise-related functionality
