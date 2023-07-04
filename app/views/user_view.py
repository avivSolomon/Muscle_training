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
            try:
                name = input("Enter your name: ")
                validations.validate_name(name)
                break
            except validations.InvalidNameException as e:
                print(e)

        # Validate email input
        while True:
            try:
                email = input("Enter your email: ")
                validations.validate_email(email)
                break
            except validations.InvalidEmailException as e:
                print(e)

        # Check if user already exists
        if self.user_controller.get_user_by_email(email) is not None:
            print("User already exists. Please login.\n")

        else:
            # Validate password input
            while True:
                try:
                    password = input("Enter your password: ")
                    validations.validate_password(password)
                    break
                except validations.InvalidPasswordException as e:
                    print(e)

            # Validate height input
            while True:
                try:
                    height = input("Enter your height in cm: ")
                    validations.validate_height(height)
                    height = int(height)
                    break
                except validations.InvalidHeightException as e:
                    print(e)

            # Validate weight input
            while True:
                try:
                    weight = input("Enter your weight in kg: ")
                    validations.validate_weight(weight)
                    weight = int(weight)
                    break
                except validations.InvalidWeightException as e:
                    print(e)

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
                try:
                    new_name = input("Enter your new name (or press Enter to skip): ")
                    if new_name == "":
                        break
                    validations.validate_name(new_name)
                    break
                except validations.InvalidNameException as e:
                    print(e)
            # Validate new_email input
            while True:
                try:
                    new_email = input("Enter your new email (or press Enter to skip): ")
                    if new_email == "":
                        break
                    validations.validate_email(new_email)
                    break
                except validations.InvalidEmailException as e:
                    print(e)
                # check if email already exists
                if self.user_controller.get_user_by_email(new_email) is not None:
                    print("User already exists.\n")
                else:
                    break
            # Validate new_password input
            while True:
                try:
                    new_password = input("Enter your new password (or press Enter to skip): ")
                    if new_password == "":
                        break
                    validations.validate_password(new_password)
                    break
                except validations.InvalidPasswordException as e:
                    print(e)

            # Validate new_height input
            while True:
                try:
                    new_height = input("Enter your new height (or press Enter to skip): ")
                    if new_height == "":
                        break
                    validations.validate_height(new_height)
                    new_height = int(new_height)
                    break
                except validations.InvalidHeightException as e:
                    print(e)
            # Validate new_weight input
            while True:
                try:
                    new_weight = input("Enter your new weight (or press Enter to skip): ")
                    if new_weight == "":
                        break
                    validations.validate_weight(new_weight)
                    new_weight = int(new_weight)
                    break
                except validations.InvalidWeightException as e:
                    print(e)
            # Update the user's details in the database
            self.user_controller.update_profile(new_name, new_email, new_password, new_height, new_weight)
            print("\nProfile updated successfully.\n")


if __name__ == "__main__":
    user_view = UserView()

