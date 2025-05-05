import socket

def tcp_fixed_length_server():
    HOST = "127.0.0.1"
    PORT = 2900
    MAX_LEN = 20

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(1)
        print(f"Serwer nasłuchuje na {HOST}:{PORT} (dokładnie {MAX_LEN} bajtów)")

        while True:
            client_socket, client_address = sock.accept()
            print(f"Połączenie od {client_address}")
            with client_socket:
                # jeśli wysylamy wiadomosc nie równa 20 znakow, zeby serwer się nie "zawiesił"
                #client_socket.settimeout(10.0)
                try:
                    data = b''
                    while len(data) < MAX_LEN:
                        chunk = client_socket.recv(MAX_LEN - len(data))
                        if not chunk:
                            break
                        data += chunk

                    received_message = data.decode("utf-8", errors="replace")
                    print(f"Otrzymano wiadomość: {received_message} ({len(data)} bajtów)")

                    adjusted_message = received_message[:MAX_LEN].ljust(MAX_LEN)
                    client_socket.sendall(adjusted_message.encode("utf-8"))
                    print(f"Wysłano wiadomość: {adjusted_message} ({len(adjusted_message.encode())} bajtów)")

                except Exception as e:
                    print(f"Błąd: {e}")

if __name__ == "__main__":
    tcp_fixed_length_server()
