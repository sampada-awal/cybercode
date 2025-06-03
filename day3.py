import string
def brute_force(password):
    chars = string.ascii_letters + string.digits + string.punctuation
    attempt=""
    for char in password:
        for c in chars:
            print(f"trying: {attempt+c}")
            if c == char:
                attempt+=c
    
    print(f"password cracked: {attempt}")

user_pwd=input("enter a password:")
brute_force(user_pwd)
