import socket
from datetime import datetime

def banner_grab(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return "No banner"

def scan_ports(ip, start_port, end_port):
    print(f"Scanning {ip} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is open")
                banner = banner_grab(ip, port)
                print(f"    Banner: {banner}")
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Scan cancelled.")
            break
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            break
        except socket.error:
            print("[!] Could not connect to server.")
            break

target = input("Enter target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

start_time = datetime.now()
scan_ports(target, start_port, end_port)
end_time = datetime.now()

print(f"\nScan completed in: {end_time - start_time}")
