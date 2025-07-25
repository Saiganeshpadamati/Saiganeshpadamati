import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    if strength == 4:
        remarks = "Strong 💪"
    elif strength == 3:
        remarks = "Moderate 🙂"
    elif strength == 2:
        remarks = "Weak 😕"
    else:
        remarks = "Very Weak ❌"

    return remarks

if _name_ == "_main_":
    password = input("Enter a password to check: ")
    print("Password Strength:", check_password_strength(password))
