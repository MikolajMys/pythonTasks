# ZAD 5
import sys
import socket

if len(sys.argv) != 2:
    print("Użyj: python zad_5.py <hostname>")
    sys.exit(1)

hostname = sys.argv[1]

try:
    ip_address = socket.gethostbyname(hostname)
    print(f"Adres ip dla {hostname}: {ip_address}")
except socket.gaierror:
    print("Nie można znaleźć adresu ip dla podanej nazwy hosta.")
