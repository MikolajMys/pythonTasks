import socket

def udp_hostname_to_ip_server():
    HOST = "127.0.0.1"
    PORT = 13

    server_address = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    print(f"Serwer UDP nasłuchuje na {HOST}:{PORT} (Hostname → IP)")

    while True:
        try:
            hostname_data, client_address = sock.recvfrom(1024)
            hostname = hostname_data.decode()
            print(f"Otrzymano hostname: {hostname}")

            try:
                ip_address = socket.gethostbyname(hostname)
            except socket.gaierror:
                ip_address = "Nie znaleziono IP dla tego hosta"

            sock.sendto(ip_address.encode(), client_address)

        except Exception as e:
            print(f"Błąd: {e}")

if __name__ == "__main__":
    udp_hostname_to_ip_server()
