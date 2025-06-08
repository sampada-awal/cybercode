import operator
def encrypt( message, key):
    message_bytes = message.encode()
    key_bytes= key.encode()
    encrypted = bytearray()
    
    for i in range(len(message_bytes)):
        encrypted_byte = message_bytes[i] ^ key_bytes[i % len(key_bytes)]
        encrypted.append(encrypted_byte)
    
    print("Encrypted bytes:", encrypted)
    

message=input("enter a message you want to encrypt:")
key=input("enter the key to be used to encrypt:")
encrypt(message,key)