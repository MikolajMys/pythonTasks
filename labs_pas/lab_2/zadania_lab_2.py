import socket
import threading

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
def check_port_service(server_address: str, port: int):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)

        print(f"Łączenie z {server_address}:{port}...")
        sock.connect((server_address, port))

        try:
            service_name = socket.getservbyport(port)
        except OSError:
            service_name = "Nieznana usługa"

        print(f"Połączenie nawiązane! Usługa: {service_name}")

        sock.close()
    except socket.gaierror:
        print("Błąd: Nie można rozpoznać adresu serwera")
    except socket.timeout:
        print("Błąd: Przekroczono czas oczekiwania na połączenie")
    except ConnectionRefusedError:
        print("Błąd: Połączenie odrzucone (port prawdopodobnie zamknięty)")
    except Exception as e:
        print(f"Błąd: {e}")

# ZAD8
def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        sock.connect((host, port))
        try:
            service_name = socket.getservbyport(port)
        except OSError:
            service_name = "Nieznana usługa"

        print(f"Port {port} jest otwarty - Usługa: {service_name}")

    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        sock.close()

def scan_ports(host, start_port=1, end_port=1024, max_threads=100):
    print(f"Skanowanie hosta {host} od portu {start_port} do {end_port}...\n")

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(host, port))
        threads.append(thread)
        thread.start()

        if len(threads) >= max_threads:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

# ZAD9
def udp_ip_to_hostname():
    # server = ("212.182.24.27", 2906)
    server = ("127.0.0.1", 2906)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ip_address = input("Podaj adres ip: ")

    sock.sendto(ip_address.encode(), server)

    try:
        data, _ = sock.recvfrom(1024)
        print("Hostname:", data.decode())

    except socket.timeout:
        print("Serwer nie odpowiedział w wyznaczonym czasie.")

    finally:
        sock.close()

# ZAD10
def udp_hostname_to_ip():
    # server = ("212.182.24.27", 2907)
    server = ("127.0.0.1", 2907)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = input("Podaj nazwę hosta: ")
    sock.sendto(hostname.encode(), server)
    data, _ = sock.recvfrom(1024)
    sock.close()
    print("Adres ip:", data.decode())

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

    print(f"Odpowiedź serwera:'{data.decode()}'")

# ZAD12
def tcp_client_single_message_fixed_length_received():
    # server = ("212.182.24.27", 2908)
    server = ("127.0.0.1", 2908)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server)

    message = input("Wpisz wiadomość (max 20 znaków): ")

    message = message[:20].ljust(20)

    total_sent = 0
    while total_sent < len(message):
        sent = sock.send(message[total_sent:].encode())
        total_sent += sent

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

# Uruchamianie zadań - odkomentowywać pojedynczo
if __name__ == "__main__":
    # ZAD 1
    # get_ntp_time()

    # ZAD 2
    # tcp_client_single_message()

    # ZAD 3
    # tcp_client_loop()

    # ZAD 4
    # udp_client_single_message()

    # ZAD 5
    # udp_client_loop()

    # ZAD 6
    # udp_math_client()

    # ZAD 7
    # server = input("Podaj adres serwera: ")
    # port = int(input("Podaj numer portu: "))
    # check_port_service(server, port)

    # ZAD 8
    # host = input("Podaj adres serwera: ")
    # start_port = int(input("Podaj początkowy port: ") or 1)
    # end_port = int(input("Podaj końcowy port: ") or 1024)
    # scan_ports(host, start_port, end_port)

    # ZAD 9
    # udp_ip_to_hostname()

    # ZAD 10
    # udp_hostname_to_ip()

    # ZAD 11
    # tcp_client_single_message_fixed_length()

    # ZAD 12
    tcp_client_single_message_fixed_length_received()
