import socket

HOST = "127.0.0.1"
PORT = 2900

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(server_address)
    print(f"Pomyślnie połączono z {HOST} na porcie {PORT}")

    message = input("Wpisz wiadomość do wysłania: ")
    sock.sendto(message.encode("utf-8"), server_address)
    print(f"Wiadomość wysłana: {message}")

    data, _ = sock.recvfrom(1024)
    print(f"Odpowiedź serwera: {data.decode()}")

except socket.error as e:
    print(f"Błąd: {e}")

sock.close()