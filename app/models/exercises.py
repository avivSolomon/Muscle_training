class Exercise:
    def __init__(self, name, duration=3, intensity=15):
        self.name = name
        self.duration = duration
        self.intensity = intensity
        self.Value_points = duration * intensity

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_intensity(self):
        return self.intensity

    def set_intensity(self, intensity):
        self.intensity = intensity


# Additional code for exercise-related functionality
