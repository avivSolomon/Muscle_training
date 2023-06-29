from app.controller.muscle_controller import MuscleController

class MuscleView:
    def __init__(self):
        self.muscle_controller = MuscleController()

    def create_muscle(self):
        name = input("Enter muscle name: ")
        description = input("Enter muscle description: ")

        # Create a new Muscle instance
        muscle = self.muscle_controller.create_muscle(name, description)

        return muscle

    def display_muscle_details(self, muscle):
        print("Muscle Details:")
        print(f"Name: {muscle.get_name()}")
        print(f"Description: {muscle.get_description()}")

    def manage_muscles(self):
        while True:
            print("\n1. Create Muscle")
            print("2. Display Muscle Details")
            print("3. Back")

            choice = input("Enter your choice: ")
            if choice == "1":
                muscle = self.create_muscle()
                print("Muscle created successfully.")
            elif choice == "2":
                muscle_name = input("Enter muscle name: ")
                muscle = self.muscle_controller.get_muscle_by_name(muscle_name)
                if muscle:
                    self.display_muscle_details(muscle)
                else:
                    print("Muscle not found.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")


# Additional code for user interface related to muscle management

if __name__ == "__main__":
    muscle_view = MuscleView()

    while True:
        print("\n1. Manage Muscles")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            muscle_view.manage_muscles()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
