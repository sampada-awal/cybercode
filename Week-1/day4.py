import socket

socket.setdefaulttimeout(1)

target=input("enter the target IP address or domain name:")

ports=[22,80,443,8080] #SSH,HTTP,HTTPS,ALT HTTP

print(f"Scanning {target}...\n")

for p in ports:
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result= s.connect_ex((target,p))
    if result==0:
        print(f"Port {p} is OPEN")
    else:
        print(f"Port {p} is CLOSED")
s.close()

