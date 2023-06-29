from exercise_controller import ExerciseController

class ExerciseView:
    def __init__(self):
        self.exercise_controller = ExerciseController()

    def create_exercise(self):
        name = input("Enter exercise name: ")
        duration = int(input("Enter exercise duration (in minutes): "))
        intensity = input("Enter exercise intensity: ")

        # Create a new Exercise instance
        exercise = self.exercise_controller.create_exercise(name, duration, intensity)

        return exercise

    def display_exercise_details(self, exercise):
        print("Exercise Details:")
        print(f"Name: {exercise.get_name()}")
        print(f"Duration: {exercise.get_duration()} minutes")
        print(f"Intensity: {exercise.get_intensity()}")

    def manage_exercises(self):
        while True:
            print("\n1. Create Exercise")
            print("2. Display Exercise Details")
            print("3. Back")

            choice = input("Enter your choice: ")
            if choice == "1":
                exercise = self.create_exercise()
                print("Exercise created successfully.")
            elif choice == "2":
                exercise_name = input("Enter exercise name: ")
                exercise = self.exercise_controller.get_exercise_by_name(exercise_name)
                if exercise:
                    self.display_exercise_details(exercise)
                else:
                    print("Exercise not found.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")


# Additional code for user interface related to exercise management

if __name__ == "__main__":
    exercise_view = ExerciseView()

    while True:
        print("\n1. Manage Exercises")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            exercise_view.manage_exercises()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
