import socket

def tcp_fixed_length_server():
    HOST = "127.0.0.1"
    PORT = 2900
    MAX_LEN = 20

    server_address = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)

    sock.listen(1)
    print(f"Serwer TCP nasłuchuje na {HOST}:{PORT} (maks. 20 znaków)")

    while True:
        client_socket, client_address = sock.accept()
        print(f"Połączenie od {client_address}")

        try:
            data = client_socket.recv(MAX_LEN)
            if data:
                received_message = data.decode()
                print(f"Otrzymano wiadomość: {received_message} ({len(data)} bajtów)")

                adjusted_message = received_message[:MAX_LEN].ljust(MAX_LEN)

                client_socket.sendall(adjusted_message.encode())
                print(f"Wysłano wiadomość: {adjusted_message} ({len(adjusted_message)} bajtów)")

        except Exception as e:
            print(f"Błąd: {e}")

        finally:
            client_socket.close()

if __name__ == "__main__":
    tcp_fixed_length_server()
