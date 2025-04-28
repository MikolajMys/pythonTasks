import socket

HOST = "127.0.0.1"
PORT = 13

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_address = input("Podaj adres IP: ")

try:
    sock.sendto(ip_address.encode(), server_address)

    data = sock.recv(1024).decode()
    print(f"Odpowiedź serwera: {data}")

except socket.error as e:
    print(f"Błąd: {e}")