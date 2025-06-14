from cryptography.fernet import Fernet
import os

def generate_key():
    """Generates a new encryption key."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads the encryption key from the file."""
    return open("secret.key", "rb").read()

def encrypt_file(file_path, key):
    """Encrypts a file using the provided key."""
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    """Decrypts a file using the provided key."""
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)


if not os.path.exists("secret.key"):
        generate_key()
key = load_key()

while True:
        choice = input("Encrypt (e) or Decrypt (d) or Exit (x)? ").lower()
        if choice == 'e':
            file_path = input("Enter the file path to encrypt: ")
            if os.path.exists(file_path):
                encrypt_file(file_path, key)
                print(f"File '{file_path}' encrypted.")
            else:
                print("File not found.")
        elif choice == 'd':
            file_path = input("Enter the file path to decrypt: ")
            if os.path.exists(file_path):
                decrypt_file(file_path, key)
                print(f"File '{file_path}' decrypted.")
            else:
                print("File not found.")
        elif choice == 'x':
            break
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'x'.")
