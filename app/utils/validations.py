# Helpers.py

def validate_email(email):
    if "@" in email:
        return True
    else:
        return False

def validate_password(password):
    if len(password) >= 6:
        return True
    else:
        return False

def validate_duration(duration):
    if duration > 0:
        return True
    else:
        return False

def validate_intensity(intensity):
    if intensity >= 1 and intensity <= 10:
        return True
    else:
        return False

def validate_name(name):
    if len(name) > 0:
        return True
    else:
        return False
