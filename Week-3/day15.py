import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "Choose at least one character set!"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    criteria = sum([has_upper, has_lower, has_digit, has_symbol])
    if length >= 12 and criteria == 4:
        return "Strong 💪"
    elif length >= 8 and criteria >= 3:
        return "Moderate ⚠️"
    else:
        return "Weak 🚫"

# User input
length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated password:", password)
print("Strength:", password_strength(password))
