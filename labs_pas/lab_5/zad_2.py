import socket
from random import randint

HOST = "127.0.0.1"
PORT = 2912
RANGE = (1, 100)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Serwer uruchomiony na {HOST}:{PORT}")
secret_number = randint(*RANGE)
print(f"(Debug) Wylosowana liczba to: {secret_number}")

try:
    connection, client_address = server_socket.accept()
    print(f"Połączenie od klienta: {client_address}")

    while True:
        data = connection.recv(1024)
        if not data:
            print("Połączenie zostało przerwane przez klienta.")
            break

        try:
            user_number = int(data.decode())
        except ValueError:
            connection.sendall("Błąd: To nie jest liczba całkowita.".encode())
            continue

        if user_number < secret_number:
            connection.sendall("Twoja liczba jest za mała.".encode())
        elif user_number > secret_number:
            connection.sendall("Twoja liczba jest za duża.".encode())
        else:
            connection.sendall("Gratulacje! Odgadłeś liczbę!".encode())
            print("Liczba została odgadnięta — zamykam serwer.")
            break

except Exception as e:
    print("Błąd serwera:", e)

finally:
    connection.close()
    server_socket.close()
