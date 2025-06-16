import re
from urllib.parse import urlparse

def is_suspicious(url):
    reasons = []

    # Check if using IP address
    if re.match(r'https?://\d+\.\d+\.\d+\.\d+', url):
        reasons.append("Uses IP address instead of domain")

    # Check for @ symbol
    if '@' in url:
        reasons.append("Contains '@' symbol")

    # Check for multiple 
    if url.count('//') > 1:
        reasons.append("Contains multiple '//'")

    # Check for very long URLs
    if len(url) > 75:
        reasons.append("URL is unusually long")

    # Check for suspicious domain (like g00gle)
    suspicious_keywords = ['login', 'secure', 'account', 'update', 'verify', 'bank', 'free', 'gift', 'g00gle', 'amaz0n']
    if any(word in url.lower() for word in suspicious_keywords):
        reasons.append("Contains suspicious keywords")

    return reasons

# ---- Main ----
user_url = input("Enter the URL to check: ").strip()
reasons = is_suspicious(user_url)

print("\nAnalysis Result:")
if reasons:
    print("This URL may be **suspicious** for the following reasons:")
    for reason in reasons:
        print(f"- {reason}")
else:
    print("This URL appears to be **legitimate**.")
