from app.models.user import User


class UserController:
    def __init__(self):
        self.current_user = None

    def is_valid_email(self, email):
        # Implement email validation logic
        return "@" in email

    def create_user(self, name, email, password):
        # Create a new User instance
        return User(name, email, password)

    def save_user(self, user):
        # Store user details in the database
        # Implement the database storage logic here
        pass

    def authenticate_user(self, email, password):
        # Authenticate user against stored credentials
        # Implement the authentication logic here
        self.current_user = ...
        return True

    def get_current_user(self):
        return self.current_user

    def update_profile(self, new_name=None, new_email=None, new_password=None):
        # Update the user's details in the database
        # Implement the update logic here
        user = self.get_current_user()
        user.set_name(new_name) if new_name is not None else user.get_name()
        user.set_email(new_email) if new_email is not None else user.get_email()
        user.set_password(new_password) if new_password is not None else user.get_password()

