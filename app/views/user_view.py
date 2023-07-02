from app.controller.user_controller import UserController


class UserView:
    def __init__(self):
        self.user_controller = UserController()

    def register_user(self):
        name = input("Enter your name: ")
        while True:
            email = input("Enter your email: ")
            # Validate inputs
            if not self.user_controller.is_valid_email(email):
                print("Invalid email format.")
            else:
                break
        password = input("Enter your password: ")

        if self.user_controller.get_user_by_email(email) is not None:
            print("User already exists.")
        else:
            height = int(input("Enter your height in cm: "))
            weight = int(input("Enter your weight in kg: "))
            self.user_controller.create_user(name, email, password, height, weight)
            print("User created successfully.")

    def login_user(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Authenticate user against stored credentials
        if self.user_controller.authenticate_user(email, password):
            print("Login successful. Welcome!")
            self.user_dashboard()
        else:
            print("Invalid email or password.")

    def user_dashboard(self):
        print("Welcome to your dashboard!")
        # Additional options and functionalities for the user's dashboard can be implemented here
        while True:
            print("1. Manage Profile")
            print("2. Manage Training Program")
            print("3. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.manage_profile()
            elif choice == "2":
                self.manage_training_program()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_profile(self):
        # Display the user's profile information
        current_user = self.user_controller.get_current_user()
        print("Profile Information:")
        print(f"Name: {current_user.get_name()}")
        print(f"Email: {current_user.get_email()}")
        print(f"Height: {current_user.get_height()}")
        print(f"Weight: {current_user.get_weight()}")
        print(f"BMI: {current_user.get_bmi()}")


        # # Allow the user to update their profile details (name, email, password)
        # choice = input("Do you want to update your profile? (yes/no): ")
        # if choice.lower() == "yes":
        #     new_name = input("Enter your new name (or press Enter to skip): ")
        #     new_email = input("Enter your new email (or press Enter to skip): ")
        #     new_password = input("Enter your new password (or press Enter to skip): ")
        #
        #     # Update the user's details in the database
        #     self.user_controller.update_profile(new_name, new_email, new_password)
        #     print("Profile updated successfully.")


# Additional code for user interface related to user management

if __name__ == "__main__":
    user_view = UserView()

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            user_view.register_user()
        elif choice == "2":
            user_view.login_user()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

