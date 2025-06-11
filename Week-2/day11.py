import requests
def scan_subdomain(domain,subdomain):
    for sub in subdomain:
        url= f"https://{subdomain}.{domain}"
        try:
            requests.get(url)
            print(f"+ {url}")
        except requests.ConnectionError:
            pass

domain_name=input("enter domain name \n")
with open('subdomain_file.txt','r') as sub_file:
    name=sub_file.read()
    subdomain_name= name.splitlines()
    
scan_subdomain(domain_name,subdomain_name)
