import socket

HOST = "127.0.0.1"
PORT = 2900

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        sock.connect((HOST, PORT))
        print(f"Połączono z {HOST}:{PORT}")

        message = input("Wpisz wiadomość do wysłania: ")
        encoded_msg = message.encode("utf-8")

        # Wyślij wiadomość (mniej niż 20 bajtów OK)
        sock.sendall(encoded_msg)
        print(f"Wysłano wiadomość: {message} ({len(encoded_msg)} bajtów)")

        # Odbierz dokładnie 20 bajtów
        data = b""
        while len(data) < 20:
            chunk = sock.recv(20 - len(data))
            if not chunk:
                break
            data += chunk

        print(f"Odpowiedź serwera: {data.decode('utf-8', errors='replace')} ({len(data)} bajtów)")

    except socket.error as e:
        print(f"Błąd: {e}")
