class TrainingProgram:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.exercises = []

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def remove_exercise(self, exercise):
        if exercise in self.exercises:
            self.exercises.remove(exercise)

    def get_exercises(self):
        return self.exercises

    def clear_exercises(self):
        self.exercises = []

    def get_program_details(self):
        program_details = f"Training Program: {self.name}\n"
        program_details += f"Duration: {self.duration} days\n"
        program_details += "Exercises:\n"

        for exercise in self.exercises:
            program_details += f"- {exercise.name}\n"

        return program_details


# Additional code for training program-related functionality
