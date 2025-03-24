# ZAD 3
import re

def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None

ip_address = input("Podaj adres ip:")
if is_valid_ip(ip_address):
    print("Poprawny adres ip")
else:
    print("Niepoprawny adres ip")