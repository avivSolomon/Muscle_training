from app.views.training_program_view import TrainingProgramView

class TrainingProgramController:
    def __init__(self):
        self.training_program_view = TrainingProgramView()

    def create_program(self, name, duration):
        return self.training_program_view.create_program(name, duration)

    def add_exercise_to_program(self, program, exercise):
        self.training_program_view.add_exercise_to_program(program, exercise)


# Additional code for training program controller functionality

if __name__ == "__main__":
    training_program_controller = TrainingProgramController()

    while True:
        print("\n1. Manage Training Program")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            training_program_controller.manage_training_program()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
