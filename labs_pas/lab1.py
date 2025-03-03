# ZAD 1
import shutil
import socket
import re

# source_file = input("Podaj nazwę pliku tekstowego:")
# shutil.copyfile(source_file, "lab1zad1.txt")

# ZAD 2
# source_file = input("Podaj nazwę pliku graficznego:")
# destination_file = "lab1zad1.png"
#
# shutil.copyfile(source_file, destination_file)

# ZAD 3
def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None
#
# ip_address = input("Podaj adres IP:")
# if is_valid_ip(ip_address):
#     print("Adres IP jest poprawny.")
# else:
#     print("Adres IP jest niepoprawny.")

# ZAD 4
ip_address = input("Podaj adress IP:")
if is_valid_ip(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)
        print(f"Nazwa hosta dla {ip_address} to {hostname}")
    except socket.herror:
        print("Nie można znaleźć nazwy hosta dla podanego adresu IP.")
else:
    print("Adres IP jest niepoprawny.")

# ZAD 5