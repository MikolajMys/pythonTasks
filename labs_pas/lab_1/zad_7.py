import sys
import socket
import threading

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((host, port))
        print(f"Port {port} jest otwarty")
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użyj: python zad_7.py <adres_serwera> [początkowy_port] [końcowy_port]")
        sys.exit(1)

    server_address = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    scan_ports(server_address, start_port, end_port)
