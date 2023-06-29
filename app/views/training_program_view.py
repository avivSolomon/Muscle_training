class TrainingProgramView:
    def create_program(self):
        name = input("Enter program name: ")
        duration = int(input("Enter program duration (in days): "))
        program = TrainingProgram(name, duration)

        return program

    def add_exercise_to_program(self, program, exercise):
        program.add_exercise(exercise)

    def display_program_details(self, program):
        program_details = program.get_program_details()
        print(program_details)


# Additional code for user interface related to training program management
