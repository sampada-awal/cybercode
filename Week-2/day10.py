import requests
def check_website_status(url):
    response=requests.get(url)
    response.raise_for_status()
    return response.status_code

urls=["https://www.google.com", "https://www.example.com"]
for url in urls:
    status=check_website_status(url)
    print(f"Status for {url}:{status}")