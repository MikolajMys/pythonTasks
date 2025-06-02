import socket


def recv_all(sock):
    data = b""
    try:
        while b"\r\n\r\n" not in data:
            data += sock.recv(1024)
        return data
    except TimeoutError:
        return data


def encode_websocket_frame(data):
    frame = bytearray()
    frame.append(0x81)

    data_bytes = data.encode("utf-8")
    length = len(data_bytes)

    if length <= 125:
        frame.append(length)
    elif 126 <= length <= 65535:
        frame.append(126)
        frame.extend([(length >> 8) & 0xFF, length & 0xFF])
    else:
        frame.append(127)
        for i in range(7, -1, -1):
            frame.append((length >> (8 * i)) & 0xFF)

    frame.extend(data_bytes)
    return frame


def websocket_client():
    remote_ip = "echo.websocket.events"
    remote_port = 80

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

    message = input("Wprowadź wiadomość do wysłania (dowolna długość): ")

    try:
        frame = encode_websocket_frame(message)
        sock.sendall(frame)
        print("Wiadomość została wysłana.")
    except Exception as e:
        print(f"Błąd przy wysyłaniu wiadomości: {e}")
        sock.close()
        return

    print("---ODPOWIEDŹ SERWERA (echo)---")
    sock.settimeout(3)
    echo_response = sock.recv(1024)
    print(echo_response)

    sock.close()


if __name__ == "__main__":
    websocket_client()
