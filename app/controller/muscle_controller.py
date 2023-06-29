from app.views.muscle_view import MuscleView

class MuscleController:
    def __init__(self):
        self.muscle_view = MuscleView()

    def create_muscle(self, name, description):
        return self.muscle_view.create_muscle(name, description)


# Additional code for muscle controller functionality

if __name__ == "__main__":
    muscle_controller = MuscleController()

    while True:
        print("\n1. Manage Muscles")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            muscle_controller.manage_muscles()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")
