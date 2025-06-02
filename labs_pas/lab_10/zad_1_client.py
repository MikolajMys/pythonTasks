import socket


def recv_all(sock):
    response = b""
    try:
        while b"\r\n\r\n" not in response:
            response += sock.recv(1024)
        return response
    except TimeoutError:
        return response


def encode_text_msg_websocket(data):
    frame = []
    frame.append(chr(129))

    data_raw = data.encode()
    length = len(data_raw)

    if length <= 125:
        frame.append(chr(length))
    elif 126 <= length <= 65535:
        frame.append(chr(126))
        frame.append(chr((length >> 8) & 255))
        frame.append(chr(length & 255))
    else:
        frame.append(chr(127))
        for i in [56, 48, 40, 32, 24, 16, 8, 0]:
            frame.append(chr((length >> i) & 255))

    encoded_message = "".join(frame).encode() + data_raw
    return encoded_message


def websocket_client():
    # remote_ip = "echo.websocket.events"
    # remote_port = 80
    remote_ip = "127.0.0.1"
    remote_port = 10000

    print(f"Nawiązywanie połączenia z {remote_ip}:{remote_port}...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect_ex((remote_ip, remote_port))

    handshake = (
        "GET /chat HTTP/1.1\r\n"
        "Host: echo.websocket.events\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "Sec-WebSocket-Protocol: chat\r\n"
        "Sec-WebSocket-Version: 13\r\n"
        "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n\r\n"
    )

    sock.sendall(handshake.encode())
    response = recv_all(sock)
    print("Odpowiedź serwera po handshake'u:\n")
    print(response.decode(errors="ignore"))

    message = input("Wpisz wiadomość do wysłania przez WebSocket: ")
    encoded = encode_text_msg_websocket(message)
    sock.sendall(encoded)
    print("Wiadomość została wysłana.")

    sock.settimeout(3)
    try:
        echo = sock.recv(1024)
        print("Odpowiedź serwera (echo):")
        print(echo)
    except socket.timeout:
        print("Brak odpowiedzi od serwera (timeout).")

    sock.close()


if __name__ == "__main__":
    websocket_client()
