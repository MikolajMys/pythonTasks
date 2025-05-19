import socket

HOST = "127.0.0.1"
PORT = 2913
UDP_SEQUENCE = [13666, 25666, 11666]

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    for udp_port in UDP_SEQUENCE:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((HOST, udp_port))

        print(f"Serwer nasłuchuje na porcie UDP: {udp_port}")

        while True:
            data, client_address = udp_socket.recvfrom(1024)

            if data:
                print(f"Odebrano dane: {data.decode()} od {client_address}")

            if data.decode() == "PING":
                print("Odpowiedź: PONG")
                udp_socket.sendto("PONG".encode(), client_address)
                break

        udp_socket.close()

    tcp_socket.bind((HOST, PORT))
    tcp_socket.listen(1)
    print(f"Serwer otwiera port TCP: {PORT} i oczekuje połączenia...")

    client_socket, client_address = tcp_socket.accept()
    print(f"Połączono z klientem: {client_address}")

    try:
        message = "Gratulacje! Odnalazłeś ukrytą usługę."
        client_socket.sendall(message.encode())
    except Exception as e:
        print(f"Błąd serwera: {e}")
    finally:
        client_socket.close()
        tcp_socket.close()
        break
