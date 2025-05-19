import socket

HOST = "127.0.0.1"
PORT = 2912

ADDRESS = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(ADDRESS)
    print(f"Połączono z serwerem {HOST} na porcie {PORT}.")

    while True:
        user_input = input("Podaj liczbę całkowitą (lub wpisz 'exit' aby zakończyć): ")

        if user_input.lower() == 'exit':
            print("Zakończono działanie klienta.")
            break

        client_socket.sendall(user_input.encode())

        response = client_socket.recv(1024).decode()
        print(f"Odpowiedź serwera: {response}")

        if "Gratulacje" in response:
            print("Zgadłeś! Kończymy grę.")
            break

except socket.error as e:
    print("Błąd połączenia z serwerem:", e)

finally:
    client_socket.close()