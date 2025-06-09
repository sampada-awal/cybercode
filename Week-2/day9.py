def load_headers(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def detect_spoofing(headers):
    from_header=""
    return_path=""
    
    for line in headers.splitlines():
        if line.lower().startswith("from:"):
          from_header= line.split(":",1)[1].strip()
        elif line.lower().startswith("return-path"):
            return_path=line.split(":",1)[1].strip().strip("<>")
    print(f"From: {from_header}")
    print(f"Return Path: {return_path}")
    if from_header and return_path:
        if from_header.lower()!= return_path.lower():
            print("Possible email spoofing detected")
        else:
            print("Email headers look clean")
    else:
        print("Missing required headers for spoofing check")
        
file_path= input("Enter the path to the email header file:")
headers= load_headers(file_path)
detect_spoofing(headers)
        