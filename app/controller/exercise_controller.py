from exercise_view import ExerciseView

class ExerciseController:
    def __init__(self):
        self.exercise_view = ExerciseView()

    def create_exercise(self, name, duration, intensity):
        return self.exercise_view.create_exercise(name, duration, intensity)


# Additional code for exercise controller functionality

if __name__ == "__main__":
    exercise_controller = ExerciseController()

    while True:
        print("\n1. Manage Exercises")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            exercise_controller.manage_exercises()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
