import socket
import datetime

def tcp_server():
    HOST = "127.0.0.1"
    PORT = 13

    server_address = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)

    sock.listen(1)
    print(f"Serwer nasłuchuje na {HOST}:{PORT}")

    while True:
        client_socket, client_address = sock.accept()
        print(f"Połączono z {client_address}")

        try:
            data = client_socket.recv(1024)
            if data:
                print(f"Otrzymano wiadomość: {data.decode()}")

                now = datetime.datetime.now()
                time_string = now.strftime("%Y-%m-%d %H:%M:%S")

                client_socket.sendall(time_string.encode())
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    tcp_server()
