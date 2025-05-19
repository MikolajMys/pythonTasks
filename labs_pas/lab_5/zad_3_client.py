import socket

#HOST = "212.182.24.27"
HOST = "127.0.0.1"
PORT = 2913

server_address = (HOST, PORT)
udp_ports = []
found_ports = 0

starting_port = 666

try:
    udp_port = starting_port

    while found_ports < 3:
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_address = (HOST, udp_port)

        print(f"Próba knockowania na {HOST}, port {udp_port}")

        try:
            udp_sock.sendto("PING".encode(), udp_address)
            data, _ = udp_sock.recvfrom(1024)

            print(f"Odpowiedź serwera: {data.decode()}")

            if data.decode() == "PONG":
                print(f"Otwarty port UDP znaleziony: {udp_port}")
                udp_ports.append(udp_port)
                found_ports += 1
                udp_port = starting_port
            else:
                udp_sock.close()
                udp_port += 1000
        except socket.error:
            udp_port += 1000

    print(f"\nZnalezione porty UDP: {udp_ports}")

    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_sock.connect(server_address)
    print(f"Pomyślnie połączono z {HOST} na porcie {PORT}")

    data = tcp_sock.recv(1024)
    print(f"Otrzymana wiadomość TCP: {data.decode()}")

except socket.error as e:
    print(f"Błąd połączenia: {e}")
