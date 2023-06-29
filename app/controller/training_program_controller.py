class TrainingProgramController:
    def create_program(self):
        training_program_view = TrainingProgramView()
        program = training_program_view.create_program()

        return program

    def add_exercise_to_program(self, program, exercise):
        training_program_view = TrainingProgramView()
        training_program_view.add_exercise_to_program(program, exercise)

    def display_program_details(self, program):
        training_program_view = TrainingProgramView()
        training_program_view.display_program_details(program)


# Additional code for training program controller functionality
