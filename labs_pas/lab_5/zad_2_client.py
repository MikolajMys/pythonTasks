import socket

server_ip = "127.0.0.1"
server_port = 2912

address = (server_ip, server_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(address)
    print(f"Połączono z serwerem {server_ip} na porcie {server_port}.")

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