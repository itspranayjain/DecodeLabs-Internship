import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    # Special character check
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    # Strength result
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


print("\n🔐 PASSWORD STRENGTH CHECKER 🔐\n")

password = input("Enter your password: ")

strength, suggestions = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if suggestions:
    print("\nSuggestions to improve password:")
    for s in suggestions:
        print(f"- {s}")
