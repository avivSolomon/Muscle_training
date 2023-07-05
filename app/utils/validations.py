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
        raise InvalidNameException("Invalid name format (only alphabets allowed).\n")


def validate_email(email):
    if "@" not in email:
        raise InvalidEmailException("Invalid email format.\n")


def validate_password(password):
    if len(password) < 6 or not password.isalnum():
        raise InvalidPasswordException("Invalid password format (minimum 6 characters, alphanumeric).\n")


def validate_height(height):
    if not height.isdigit() or not 0 < int(height) < 300:
        raise InvalidHeightException("Invalid height format (0 < height < 300).\n")


def validate_weight(weight):
    if not weight.isdigit() or not 0 < int(weight) < 300:
        raise InvalidWeightException("Invalid weight format (0 < weight < 300).\n")



