from training_program_controller import TrainingProgramController

class TrainingProgramView:
    def __init__(self):
        self.training_program_controller = TrainingProgramController()

    def create_program(self):
        name = input("Enter program name: ")
        duration = int(input("Enter program duration (in days): "))

        # Create a new TrainingProgram instance
        program = self.training_program_controller.create_program(name, duration)

        return program

    def add_exercise_to_program(self, program):
        exercise_name = input("Enter exercise name: ")
        exercise_duration = int(input("Enter exercise duration (in minutes): "))
        exercise_intensity = input("Enter exercise intensity: ")

        # Create a new Exercise instance
        exercise = self.training_program_controller.create_exercise(exercise_name, exercise_duration, exercise_intensity)

        # Add the exercise to the training program
        self.training_program_controller.add_exercise_to_program(program, exercise)
        print("Exercise added to the program.")

    def display_program_details(self, program):
        program_details = program.get_program_details()
        print(program_details)

    def manage_training_program(self):
        program = self.create_program()

        while True:
            print("\n1. Add Exercise")
            print("2. Display Program Details")
            print("3. Back")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_exercise_to_program(program)
            elif choice == "2":
                self.display_program_details(program)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")


# Additional code for user interface related to training program management

if __name__ == "__main__":
    training_program_view = TrainingProgramView()

    while True:
        print("\n1. Create Training Program")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            training_program_view.manage_training_program()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
