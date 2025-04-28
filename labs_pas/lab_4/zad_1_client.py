import socket

HOST = "127.0.0.1"
PORT = 13

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(server_address)
    print(f"Połączono pomyślnie z {HOST} na porcie {PORT}")

    message = input("Wpisz dowolną wiadomość: ")
    sock.sendall(message.encode())

    data = sock.recv(1024).decode()
    print(f"Odpowiedź serwera: {data}")

except socket.error as e:
    print(f"Błąd: {e}")

sock.close()