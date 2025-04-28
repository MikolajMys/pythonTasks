import socket


def message_length(message, max_length, allow_oversize):
    if len(message) < max_length:
        message += " " * (max_length - len(message))
    elif len(message) > max_length:
        if not allow_oversize:
            message = message[:max_length]

    return message

HOST = "127.0.0.1"
PORT = 2900
MAX_LENGTH = 20

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(server_address)
    print(f"Pomyślnie połączono z {HOST} na porcie {PORT}")

    message = input("Enter message to send: ")
    message = message_length(message, MAX_LENGTH, True)

    sock.sendto(message.encode("utf-8"), server_address)
    print(f"Wiadomość wysłana: {message}")

    data, _ = sock.recvfrom(1024)
    print(f"Odpowiedź serwera: {data.decode()}")

except socket.error as e:
    print(f"Błąd: {e}")

sock.close()