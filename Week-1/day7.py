def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if part != str(num):  
            return False
    return True

ip = input("Enter an IP address to validate: ")
if is_valid_ip(ip):
    print("Valid IPv4 address.")
else:
    print("Invalid IPv4 address.")
