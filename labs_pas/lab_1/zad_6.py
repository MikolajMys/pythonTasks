# ZAD 6
import sys
import socket

if len(sys.argv) != 3:
    print("Użyj: python zad_6.py <adres_serwera> <port>")
    sys.exit(1)

server_address = sys.argv[1]
port = int(sys.argv[2])

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    print(f"Łączenie z {server_address}:{port}...")
    sock.connect((server_address, port))

    print("Połączenie nawiązane!")
    sock.close()
except socket.gaierror:
    print("Błąd: Nie można rozpoznać adresu serwera")
except socket.timeout:
    print("Błąd: Przekroczono czas oczekiwania na połączenie")
except ConnectionRefusedError:
    print("Błąd: Połączenie odrzucone")
except Exception as e:
    print(f"Błąd: {e}")
