import socket
import threading

def handle_client(client_socket, addr):
    print(f"[TCP] Połączono z {addr}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[TCP] Otrzymano: {data.decode()}")
            client_socket.sendall(b"Echo: " + data)
        except ConnectionResetError:
            break
    client_socket.close()
    print(f"[TCP] Rozłączono: {addr}")

def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 2700))
    server.listen(5)
    print("[TCP] Serwer nasłuchuje na porcie 2700")

    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

if __name__ == "__main__":
    tcp_server()
