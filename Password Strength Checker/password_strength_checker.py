import re

def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Check for at least one lowercase letter
    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter."

    # Check for at least one uppercase letter
    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    # Check for at least one digit
    if not re.search("[0-9]", password):
        return "Password must contain at least one digit."

    # Check for at least one special character
    if not re.search("[@#$%^&+=]", password):
        return "Password must contain at least one special character (@, #, $, %, ^, &, +, =)."

    # If all conditions are met
    return "Password is strong."

# Get user input
password = input("Enter your password: ")

# Check the password strength
result = check_password_strength(password)

# Print the result
print(result)
