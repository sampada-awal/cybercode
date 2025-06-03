import re
def password_check(password):
    length_error=len(password)<8
    digit_error=re.search(r"\d",password) is None
    uppercase_error=re.search(r"[A-Z]",password) is None
    lowercase_error=re.search(r"[a-z]",password) is None
    symbol_error=re.search(r"[!@#$&^*]",password) is None
    
    error=[length_error,digit_error,uppercase_error,lowercase_error,symbol_error]
    if any(error):
       print("weak password")
    else: 
       print("strong password")

password=input("Enter your password:")
password_check(password)
