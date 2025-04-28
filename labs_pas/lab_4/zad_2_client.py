import socket

def tcp_client():
    HOST = "127.0.0.1"
    PORT = 13

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        print(f"Połączono z serwerem {HOST}:{PORT}")

        message = input("Podaj wiadomość do wysłania: ")
        sock.sendall(message.encode())

        data = sock.recv(1024)
        print("Odebrano od serwera:", data.decode())

    except socket.error as e:
        print(f"Błąd gniazda: {e}")

    finally:
        sock.close()

if __name__ == "__main__":
    tcp_client()
