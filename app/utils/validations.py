class InvalidOptionException(Exception):
    pass


class InvalidNameException(Exception):
    pass


class InvalidEmailException(Exception):
    pass


class InvalidPasswordException(Exception):
    pass


class InvalidHeightException(Exception):
    pass


class InvalidWeightException(Exception):
    pass


def validate_name(name):
    if len(name) == 0 or not name.isalpha():
        raise InvalidNameException("Invalid name format (only alphabets allowed).")


def validate_email(email):
    if "@" not in email:
        raise InvalidEmailException("Invalid email format.")


def validate_password(password):
    if len(password) < 6 or not password.isalnum():
        raise InvalidPasswordException("Invalid password format (minimum 6 characters, alphanumeric).")


def validate_height(height):
    if not height.isdigit() or not 0 < int(height) < 300:
        raise InvalidHeightException("Invalid height format (0 < height < 300).")


def validate_weight(weight):
    if not weight.isdigit() or not 0 < int(weight) < 300:
        raise InvalidWeightException("Invalid weight format (0 < weight < 300).")


# def validate_opening_page_input(option):
#     if option not in ["1", "2", "3"]:
#         raise InvalidOptionException("Invalid input. Please enter a number between 1 and 4.")
#
#
# def validate_user_dashboard_input(option):
#     if option not in ["1", "2", "3"]:
#         raise InvalidOptionException("Invalid input. Please enter a number between 1 and 3.")
#
#
# def validate_manage_profile_input(option):
#     if option.lower() not in ["yes", "no", "y", "n"]:
#         raise InvalidOptionException("Invalid input. Please enter yes or no.")
#
#
# def validate_training_program_input(option):
#     if option not in ["1", "2", "3", "4", "5", "6"]:
#         raise InvalidOptionException("Invalid input. Please enter a number between 1 and 6.")


