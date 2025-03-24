import socket
import datetime

def ntp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 13))
    server.listen(5)
    print("[NTP] Server listening on port 13")
    while True:
        client, addr = server.accept()
        print(f"[NTP] Connection from {addr}")
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client.sendall(now.encode())
        client.close()

if __name__ == "__main__":
    ntp_server()
