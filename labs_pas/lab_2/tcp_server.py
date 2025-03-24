import socket

def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 2900))
    server.listen(5)
    print("[TCP] Server listening on port 2900")
    while True:
        client, addr = server.accept()
        print(f"[TCP] Connection from {addr}")
        while True:
            data = client.recv(1024)
            if not data:
                break
            print(f"[TCP] Received: {data.decode()}")
            client.sendall(b"Echo: " + data)
        client.close()

if __name__ == "__main__":
    tcp_server()