import socket

#HOST = "212.182.24.27"
HOST = "127.0.0.1"
PORT = 2912

def main():
    while True:
        try:
            number = input("Podaj liczbę całkowitą (1–10) lub wpisz 'exit' aby zakończyć: ")

            if number.lower() == 'exit':
                print("Zakończono działanie klienta.")
                break

            int(number)
        except ValueError:
            print("To nie jest poprawna liczba całkowita.")
            continue

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((HOST, PORT))
                client_socket.sendall(number.encode())

                while True:
                    response = client_socket.recv(4096)
                    if not response:
                        break
                    print("Odpowiedź serwera:", response.decode())

        except Exception as e:
            print("Wystąpił błąd podczas komunikacji z serwerem:", e)

if __name__ == "__main__":
    main()
