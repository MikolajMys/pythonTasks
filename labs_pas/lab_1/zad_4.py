# ZAD 4
import socket
import re

def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None
ip_address = input("Podaj adress ip:")
if is_valid_ip(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)
        print(f"Nazwa hosta dla {ip_address} to {hostname}")
    except socket.herror:
        print("Nie można znaleźć nazwy hosta")
else:
    print("Niepoprawny adres ip")
