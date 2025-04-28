import socket

HOST = "127.0.0.1"
PORT = 13

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    message = input("Wpisz dowolną wiadomość: ")
    sock.sendto(message.encode(), server_address)

    data = sock.recv(1024).decode()
    print(f"Odpowiedź serwera: {data}")

except socket.error as e:
    print(f"Błąd: {e}")

sock.close()