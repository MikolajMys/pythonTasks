import socket


def recv_all(sock):
    data = b""
    try:
        while b"\r\n\r\n" not in data:
            data += sock.recv(1024)
        return data
    except TimeoutError:
        return data


def encode_text_msg_websocket(data):
    frame = bytearray()
    frame.append(0x81)

    data_bytes = data.encode("utf-8")
    data_length = len(data_bytes)

    if data_length > 125:
        raise ValueError("Za długa (maks. 125 bajtów)")

    frame.append(data_length)
    frame += data_bytes
    return frame


def websocket_client():
    #remote_ip = "echo.websocket.events"
    #remote_port = 80

    remote_ip = "127.0.0.1"
    remote_port = 10000

    print(f"Nawiązywanie połączenia z {remote_ip}:{remote_port}...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((remote_ip, remote_port))

    handshake = (
        "GET / HTTP/1.1\r\n"
        "Host: echo.websocket.events\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "Sec-WebSocket-Version: 13\r\n"
        "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n\r\n"
    )

    sock.sendall(handshake.encode())
    response = recv_all(sock)
    print("Odpowiedź po handshake'u:\n")
    print(response.decode(errors="ignore"))

    message = input("Podaj wiadomość do wyslania (max 125 znaków): ")

    try:
        frame = encode_text_msg_websocket(message)
        sock.sendall(frame)
        print("Wiadomość została wysłana.")
    except Exception as e:
        print(f"Błąd przy wysyłaniu wiadomości: {e}")
        sock.close()
        return

    print("---ODPOWIEDŹ SERWERA---")
    sock.settimeout(3)
    echo_response = sock.recv(1024)
    print(echo_response)

    sock.close()


if __name__ == "__main__":
    websocket_client()
