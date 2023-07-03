def is_valid_name(name):
    return len(name) > 0 and name.isalpha()


def is_valid_email(email):
    # Implement email validation logic
    return "@" in email


def is_valid_password(password):
    # Implement password validation logic
    return len(password) >= 6 and password.isalnum()

def is_valid_height(height):
    return height.isdigit() and 0 < int(height) < 300

def is_valid_weight(weight):
    return weight.isdigit() and 0 < int(weight) < 300