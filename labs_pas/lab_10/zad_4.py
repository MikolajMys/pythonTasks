import socket
import base64
import hashlib


def create_websocket_accept_key(sec_websocket_key):
    magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    accept_raw = sec_websocket_key + magic_string
    accept_hash = hashlib.sha1(accept_raw.encode()).digest()
    accept_key = base64.b64encode(accept_hash).decode()
    return accept_key


def decode_websocket_frame(frame):
    payload_length = frame[1] & 127
    if payload_length == 126:
        mask = frame[4:8]
        data = frame[8:]
    elif payload_length == 127:
        mask = frame[10:14]
        data = frame[14:]
    else:
        mask = frame[2:6]
        data = frame[6:]
    decoded = bytearray()
    for i in range(len(data)):
        decoded.append(data[i] ^ mask[i % 4])
    return decoded.decode('utf-8', errors='ignore')


def encode_websocket_frame(data):
    payload = data.encode('utf-8')
    frame = bytearray()
    frame.append(129)
    length = len(payload)
    if length <= 125:
        frame.append(length)
    elif length <= 65535:
        frame.append(126)
        frame.append((length >> 8) & 255)
        frame.append(length & 255)
    else:
        frame.append(127)
        for shift in [56, 48, 40, 32, 24, 16, 8, 0]:
            frame.append((length >> shift) & 255)
    frame += payload
    return frame


def websocket_server():
    host = "127.0.0.1"
    port = 10000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((host, port))
        server_sock.listen(1)
        print(f"Serwer nasłuchuje na {host}:{port}")

        conn, addr = server_sock.accept()
        print(f"Połączono z klientem: {addr}")

        request = conn.recv(1024).decode()
        print("Otrzymano żądanie handshake od klienta:")
        print(request)

        headers = {}
        for line in request.split("\r\n")[1:]:
            if ": " in line:
                key, value = line.split(": ", 1)
                headers[key] = value

        sec_websocket_key = headers.get("Sec-WebSocket-Key", "")
        accept_key = create_websocket_accept_key(sec_websocket_key)

        response = (
            "HTTP/1.1 101 Switching Protocols\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Accept: {accept_key}\r\n\r\n"
        )
        conn.sendall(response.encode())
        print("Handshake zakończony pomyślnie.")

        while True:
            try:
                frame = conn.recv(1024)
                if not frame:
                    break
                decoded_message = decode_websocket_frame(frame)
                print(f"Otrzymano wiadomość: {decoded_message}")

                response_frame = encode_websocket_frame(decoded_message)
                conn.sendall(response_frame)
                print("Wysłano echo do klienta.")
            except Exception as e:
                print(f"Błąd połączenia: {e}")
                break

        conn.close()
        print("Połączenie zakończone.")


if __name__ == "__main__":
    websocket_server()
