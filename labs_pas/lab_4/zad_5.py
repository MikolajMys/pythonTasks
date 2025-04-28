import socket

def udp_ip_to_hostname_server():
    HOST = "127.0.0.1"
    PORT = 13

    server_address = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    print(f"Serwer UDP nasłuchuje na {HOST}:{PORT} (IP → Hostname)")

    while True:
        try:
            ip_data, client_address = sock.recvfrom(1024)
            ip_address = ip_data.decode()
            print(f"Otrzymano adres IP: {ip_address}")

            try:
                hostname = socket.gethostbyaddr(ip_address)[0]
            except socket.herror:
                hostname = "Brak nazwy hosta dla tego IP"

            sock.sendto(hostname.encode(), client_address)

        except Exception as e:
            print(f"Błąd: {e}")

if __name__ == "__main__":
    udp_ip_to_hostname_server()
