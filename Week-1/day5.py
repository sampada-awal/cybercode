import re

def validate_email(email):
    pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern,email):
        print(f"Email {email} is valid")
    else:
        print(f"Email {email} is not valid")

email=input("Enter your email:")
validate_email(email)