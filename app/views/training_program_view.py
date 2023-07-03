from app.controller.training_program_controller import TrainingProgramController


class TrainingProgramView:
    def __init__(self, user_id):
        self.user_id = user_id
        self.training_program_controller = TrainingProgramController(user_id)
        self.display_training_program_menu()

    def display_training_program_menu(self):
        while True:
            print("\n1. Show Today's Exercises")
            print("2. Show Training Program Details")
            print("3. Create New Training Program")
            print("4. Workout")
            print("5. Show Muscles Status")
            print("6. Back")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_today_exercises()
            elif choice == "2":
                self.display_user_program_details()
            elif choice == "3":
                self.training_program_controller.create_program(self.user_id)
                print("New training program created.")
            elif choice == "4":
                self.training_program_controller.workout()
            elif choice == "5":
                self.display_muscles_status()
            elif choice == "6":
                break

    def display_today_exercises(self):
        today_exercises = self.training_program_controller.get_today_exercises()
        if today_exercises is None:
            print("No exercises for today.")
        else:
            for exercise in today_exercises:
                print(f" exercise name: {exercise[3]} \n"
                      f" exercise intensity: {exercise[4]} \n sets: {exercise[5]} \n reps: {exercise[6]} \n")

    def display_user_program_details(self):
        print(self.training_program_controller.get_user_program())

    def display_muscles_status(self):
        muscle_status = self.training_program_controller.get_muscles_status()
        for muscle in muscle_status:
            print(f"Muscle Name: {muscle[1]}\n Muscle Points: {muscle[2]}\n Workout Date: {muscle[3]}\n Rest Time: {muscle[4]}\n")

    # def manage_training_program(self):
    #     program = self.create_program()
    #
    #     while True:
    #         print("\n1. Add Exercise")
    #         print("2. Display Program Details")
    #         print("3. Back")
    #
    #         choice = input("Enter your choice: ")
    #         if choice == "1":
    #             self.add_exercise_to_program(program)
    #         elif choice == "2":
    #             self.display_program_details(program)
    #         elif choice == "3":
    #             break
    #         else:
    #             print("Invalid choice. Please try again.")


# Additional code for user interface related to training program management

if __name__ == "__main__":
    a = TrainingProgramView(1)
    # a.user_program_dashboard()


