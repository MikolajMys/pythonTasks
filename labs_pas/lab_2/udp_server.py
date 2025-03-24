import socket

def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("0.0.0.0", 2901))
    print("[UDP] Server listening on port 2901")
    while True:
        data, addr = server.recvfrom(1024)
        print(f"[UDP] Received from {addr}: {data.decode()}")
        server.sendto(b"Echo: " + data, addr)

if __name__ == "__main__":
    udp_server()
