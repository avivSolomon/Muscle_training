from user_view import UserView

class UserController:
    def __init__(self):
        self.user_view = UserView()

    def register_user(self):
        self.user_view.register_user()

    def login_user(self):
        self.user_view.login_user()

    def manage_profile(self):
        self.user_view.manage_profile()


# Additional code for user controller functionality

if __name__ == "__main__":
    user_controller = UserController()

    while True:
        print("\n1. Register User")
        print("2. Login User")
        print("3. Manage Profile")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            user_controller.register_user()
        elif choice == "2":
            user_controller.login_user()
        elif choice == "3":
            user_controller.manage_profile()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
