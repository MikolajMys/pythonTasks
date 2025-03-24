import socket

# ZAD1
def get_ntp_time():
    #server = ("ntp.task.gda.pl", 13)
    server = ("127.0.0.1", 13)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server)
    data = sock.recv(1024).decode()
    sock.close()
    print("Data i czas:", data)

# ZAD2
def tcp_client_single_message():
    # server = ("212.182.24.27", 2900)
    server = ("127.0.0.1", 2900)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server)
    sock.sendall(b"Hello, server!")
    data = sock.recv(1024)
    sock.close()
    print("Odpowiedź serwera:", data.decode())

# ZAD3
def tcp_client_loop():
    # server = ("212.182.24.27", 2900)
    server = ("127.0.0.1", 2900)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server)
    while True:
        message = input("Wpisz wiadomość: ")
        if message.lower() == "exit":
            break
        sock.sendall(message.encode())
        data = sock.recv(1024)
        print("Odpowiedź:", data.decode())
    sock.close()

# ZAD4
def udp_client_single_message():
    # server = ("212.182.24.27", 2901)
    server = ("127.0.0.1", 2901)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(b"Hello, UDP Server!", server)
    data, _ = sock.recvfrom(1024)
    sock.close()
    print("Odpowiedź serwera:", data.decode())

# ZAD5
def udp_client_loop():
    # server = ("212.182.24.27", 2901)
    server = ("127.0.0.1", 2901)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input("Wpisz wiadomość: ")
        if message.lower() == "exit":
            break
        sock.sendto(message.encode(), server)
        data, _ = sock.recvfrom(1024)
        print("Odpowiedź:", data.decode())
    sock.close()

# ZAD6
def udp_math_client():
    # server = ("212.182.24.27", 2902)
    server = ("127.0.0.1", 2902)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    num1 = input("Podaj pierwszą liczbę: ")
    operator = input("Podaj operator (+, -, *, /): ")
    num2 = input("Podaj drugą liczbę: ")

    message = f"{num1} {operator} {num2}"
    sock.sendto(message.encode(), server)
    data, _ = sock.recvfrom(1024)
    sock.close()

    print("Wynik:", data.decode())

# ZAD7

# ZAD8

# ZAD9
def udp_ip_to_hostname():
    server = ("127.0.0.1", 2906)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ip_address = input("Podaj adres IP: ")

    # Wysyłanie adresu IP w odpowiednim formacie bajtów
    sock.sendto(ip_address.encode(), server)

    try:
        # Odbieranie odpowiedzi od serwera
        data, _ = sock.recvfrom(1024)
        print("Hostname:", data.decode())  # Wyświetlanie wyniku z serwera

    except socket.timeout:
        print("Serwer nie odpowiedział w wyznaczonym czasie.")

    finally:
        sock.close()  # Zamykanie gniazda po zakończeniu komunikacji

# ZAD10
def udp_hostname_to_ip():
    # server = ("212.182.24.27", 2907)
    server = ("127.0.0.1", 2907)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = input("Podaj nazwę hosta: ")
    sock.sendto(hostname.encode(), server)
    data, _ = sock.recvfrom(1024)
    sock.close()
    print("Adres IP:", data.decode())

# ZAD11
def tcp_client_single_message_fixed_length():
    # server = ("212.182.24.27", 2908)
    server = ("127.0.0.1", 2908)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server)

    message = input("Wpisz wiadomość (max 20 znaków): ")

    message = message[:20].ljust(20)

    sock.sendall(message.encode())

    data = sock.recv(20)

    sock.close()

    print("Odpowiedź serwera:", data.decode())

# ZAD12
def tcp_client_single_message_fixed_length_received():
    # server = ("212.182.24.27", 2908)
    server = ("127.0.0.1", 2908)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server)

    message = input("Wpisz wiadomość (max 20 znaków): ")

    # Przycinanie wiadomości do 20 znaków lub uzupełnianie spacjami do 20
    message = message[:20].ljust(20)

    # Wysyłanie wiadomości do serwera, aż cała wiadomość zostanie wysłana
    total_sent = 0
    while total_sent < len(message):
        sent = sock.send(message[total_sent:].encode())
        total_sent += sent

    # Odbieranie danych od serwera
    received_data = b""
    total_received = 0
    while total_received < 20:
        chunk = sock.recv(20 - total_received)
        if not chunk:
            raise RuntimeError("Połączenie zostało zamknięte")
        received_data += chunk
        total_received += len(chunk)

    sock.close()

    print("Odpowiedź serwera:", received_data.decode())

# Uruchamianie funkcji testowych
if __name__ == "__main__":
    # get_ntp_time()
    # tcp_client_single_message()
    # tcp_client_loop()
    # udp_client_single_message()
    # udp_client_loop()
    # udp_math_client()
    udp_ip_to_hostname()
    # udp_hostname_to_ip()
    # tcp_client_single_message_fixed_length()
    # tcp_client_single_message_fixed_length_received()
