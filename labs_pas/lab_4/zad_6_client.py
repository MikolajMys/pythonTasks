import socket

HOST = "127.0.0.1"
PORT = 13

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = input("Podaj nazwę hosta: ")

try:
    sock.sendto(hostname.encode(), server_address)

    data = sock.recv(1024).decode()
    print(f"Odpowiedź serwera: {data}")

except socket.error as e:
    print(f"Błąd: {e}")