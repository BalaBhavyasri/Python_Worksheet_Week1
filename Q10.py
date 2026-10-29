def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must have at least 8 characters")

    if not any(char.isupper() for char in password):
        errors.append("Must contain an uppercase letter")

    if not any(char.islower() for char in password):
        errors.append("Must contain a lowercase letter")

    if not any(char.isdigit() for char in password):
        errors.append("Must contain a digit")

    special_chars = "!@#$%^&*"

    if not any(char in special_chars for char in password):
        errors.append("Must contain a special character")

    return {
        'is_valid': len(errors) == 0,
        'errors': errors
    }

print(validate_password("weak"))
print(validate_password("Weak123"))
print(validate_password("MySecure@1"))