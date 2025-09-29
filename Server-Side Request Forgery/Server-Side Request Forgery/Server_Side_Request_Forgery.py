import validators
import ipaddress
from urllib.parse import urlparse

def is_safe_url(url):
    if not validators.url(url):
        return False
    hostname = urlparse(url).hostname
    try:
        ip = ipaddress.ip_address(hostname)
        if ip.is_private or ip.is_loopback:
            return False
    except ValueError:
        pass
    return True

url = input("Enter URL: ")
if not is_safe_url(url):
    raise ValueError("Unsafe or invalid URL")

response = requests.get(url, timeout=5)
print(response.text)