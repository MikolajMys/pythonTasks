import socket

HOST = "127.0.0.1"
PORT = 13

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

sock.listen(1)

print(f"Serwer nasłuchuje na {HOST}:{PORT}")

while True:
    client_socket, client_address = sock.accept()
    print(f"Połączenie od {client_address}")

    try:
        data, addr = client_socket.recvfrom(1024)
        if data:
            client_socket.sendall(data)

    except Exception as e:
        print(f"Wystąpił błąd: {e}")