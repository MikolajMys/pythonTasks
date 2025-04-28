import socket

def udp_server():
    HOST = "127.0.0.1"
    PORT = 13

    server_address = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    print(f"Serwer UDP nasłuchuje na {HOST}:{PORT}")

    while True:
        try:
            data, client_address = sock.recvfrom(1024)
            print(f"Otrzymano od {client_address}: {data.decode()}")

            if data:
                sock.sendto(data, client_address)
        except Exception as e:
            print(f"Błąd: {e}")

if __name__ == "__main__":
    udp_server()
