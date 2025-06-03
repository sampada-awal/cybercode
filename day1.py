def caesar_cipher(text, shift, decrypt=False):
    result = ''
    if decrypt:
        shift = -shift
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')  # could also use 97 and 65
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            shifted_char = char
        result += shifted_char
    return result

# Test the function
plaintext = "coding day one"
shift_amt = 3
ciphertext = caesar_cipher(plaintext, shift_amt)

print(f"Plain text is: {plaintext}")
print(f"Cipher text is: {ciphertext}")

decrypted_text = caesar_cipher(ciphertext, shift_amt, decrypt=True)
print(f"Decrypted text is: {decrypted_text}")
