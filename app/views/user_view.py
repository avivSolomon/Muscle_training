from app.controller.user_controller import UserController
from app.views.training_program_view import TrainingProgramView
import app.utils.validations as validations


class UserView:
    def __init__(self):
        self.user_id = None
        self.user_controller = UserController()
        self.training_program_view = None
        self.opening_page()

    def opening_page(self):
        print("Welcome to the Fitness App!")
        while True:
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("\nEnter your choice: ")
            if choice == "1":
                self.login_user()
            elif choice == "2":
                self.register_user()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.\n")

    def register_user(self):
        print("\nWelcome to the registration page!\n")
        # Get user details
        # Validate name input
        while True:
            name = input("Enter your name: ")
            if not validations.is_valid_name(name):
                print("Invalid name format (only alphabets allowed).\n")
            else:
                break

        # Validate email input
        while True:
            email = input("Enter your email: ")
            # Validate inputs
            if not validations.is_valid_email(email):
                print("Invalid email format.\n")
            else:
                break

        # Validate password input
        while True:
            password = input("Enter your password: ")
            if not validations.is_valid_password(password):
                print("Invalid password format (minimum 6 characters, alphanumeric).\n")
            else:
                break
        # Check if user already exists
        if self.user_controller.get_user_by_email(email) is not None:
            print("User already exists. Please login.\n")
        else:
            # Validate height input
            while True:
                height = input("Enter your height in cm: ")
                if not validations.is_valid_height(height):
                    print("Invalid height format (0 < height < 300).\n")
                else:
                    height = int(height)
                    break

            # Validate weight input
            while True:
                weight = input("Enter your weight in kg: ")
                if not validations.is_valid_weight(weight):
                    print("Invalid weight format (0 < weight < 300).\n")
                else:
                    weight = int(weight)
                    break

            self.user_controller.create_user(name, email, password, height, weight)
            print("\nUser created successfully.\n")

    def login_user(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Authenticate user against stored credentials
        if self.user_controller.authenticate_user(email, password):
            print("\nLogin successful. Welcome!")
            self.user_id = self.user_controller.get_current_user().get_id()
            self.user_dashboard()
        else:
            print("Invalid email or password.\n")

    def user_dashboard(self):
        print("\nWelcome to your dashboard!")
        # Additional options and functionalities for the user's dashboard can be implemented here
        while True:
            print("1. Manage Profile")
            print("2. Manage Training Program")
            print("3. Logout")

            choice = input("\nEnter your choice: ")
            if choice == "1":
                self.manage_profile()
            elif choice == "2":
                self.training_program_view = TrainingProgramView(self.user_id)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.\n")

    def manage_profile(self):
        # Display the user's profile information
        current_user = self.user_controller.get_current_user()
        print("\nProfile Information:")
        print(f"\tName: {current_user.get_name()}")
        print(f"\tEmail: {current_user.get_email()}")
        print(f"\tHeight: {current_user.get_height()}")
        print(f"\tWeight: {current_user.get_weight()}")
        print(f"\tBMI: {current_user.get_bmi()}")

        # Allow the user to update their profile details (name, email, password)
        choice = input("\nDo you want to update your profile? (yes/no): ")
        if choice.lower() == "yes":
            # Get new details
            # Validate new_name input
            while True:
                new_name = input("Enter your new name (or press Enter to skip): ")
                if new_name == "":
                    break
                elif not validations.is_valid_name(new_name):
                    print("Invalid name format (only alphabets allowed).\n")
                else:
                    break
            # Validate new_email input
            while True:
                new_email = input("Enter your new email (or press Enter to skip): ")
                # Validate inputs
                if new_email == "":
                    break
                elif not validations.is_valid_email(new_email):
                    print("Invalid email format.\n")
                # check if email already exists
                elif self.user_controller.get_user_by_email(new_email) is not None:
                    print("User already exists.\n")
                else:
                    break
            # Validate new_password input
            while True:
                new_password = input("Enter your new password (or press Enter to skip): ")
                if new_password == "":
                    break
                elif not validations.is_valid_password(new_password):
                    print("Invalid password format (minimum 6 characters, alphanumeric).\n")
                else:
                    break
            # Validate new_height input
            while True:
                new_height = input("Enter your new height (or press Enter to skip): ")
                if new_height == "":
                    break
                elif not validations.is_valid_height(new_height):
                    print("Invalid height format (0 < height < 300).\n")
                else:
                    new_height = int(new_height)
                    break
            # Validate new_weight input
            while True:
                new_weight = input("Enter your new weight (or press Enter to skip): ")
                if new_weight == "":
                    break
                elif not validations.is_valid_weight(new_weight):
                    print("Invalid weight format (0 < weight < 300).\n")
                else:
                    new_weight = int(new_weight)
                    break
            # Update the user's details in the database
            self.user_controller.update_profile(new_name, new_email, new_password, new_height, new_weight)
            print("\nProfile updated successfully.\n")


if __name__ == "__main__":
    user_view = UserView()

