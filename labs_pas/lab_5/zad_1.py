import socket
from random import randint

HOST = "127.0.0.1"
PORT = 2912
RANGE = (1, 10)

address = (HOST, PORT)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(1)

print(f"Serwer nasłuchuje na {HOST}:{PORT}")

while True:
    connection, client_addr = server_socket.accept()
    print(f"Połączenie od {client_addr}")

    try:
        data = connection.recv(4096)
        try:
            guessed_number = int(data)
        except ValueError:
            response = "Wprowadzona wartość nie jest liczbą całkowitą."
            connection.sendall(response.encode())
            connection.close()
            continue

        if guessed_number < RANGE[0] or guessed_number > RANGE[1]:
            response = f"Liczba poza zakresem! Dozwolony zakres to: {RANGE[0]}–{RANGE[1]}"
            connection.sendall(response.encode())
        else:
            drawn_number = randint(RANGE[0], RANGE[1])
            response = f"Wylosowana liczba to: {drawn_number}"
            connection.sendall(response.encode())

            print(f"Podano: {guessed_number}, Wylosowano: {drawn_number}")

            if guessed_number == drawn_number:
                response = "Gratulacje! Trafiłeś!"
            else:
                response = "Niestety, nie tym razem."
            connection.sendall(response.encode())

    except Exception as e:
        print("Błąd:", e)

    finally:
        connection.close()
