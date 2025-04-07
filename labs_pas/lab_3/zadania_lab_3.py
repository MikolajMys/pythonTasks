import socket

def hex_to_dec(val):
    return int(val, 16)

def hex_to_ascii(val):
    return bytes.fromhex(val).decode()

tcp_segment = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
udp_datagram = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
ip_packet = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e"


def get_bytes(array, size, start_pos):
    return array[start_pos:start_pos+size]

#ZAD13
def process_udp_datagram(udp_datagram):
    data_bytes = udp_datagram.replace('\n', ' ').split()
    source_port_hex = get_bytes(data_bytes, 2, 0)
    destination_port_hex = get_bytes(data_bytes, 2, 2)
    length_hex = get_bytes(data_bytes, 2, 4)
    data_hex = data_bytes[8:]

    source_port = hex_to_dec("".join(source_port_hex))
    destination_port = hex_to_dec("".join(destination_port_hex))
    length = hex_to_dec("".join(length_hex))
    data_length = length - 8

    data_ascii = hex_to_ascii("".join(data_hex[:data_length]))

    message = f"zad14odp;src;{source_port};dst;{destination_port};data;{data_ascii}"
    print("Wiadomość do wysłania:", message)

    #HOST = "212.182.24.27"
    HOST = "127.0.0.1"
    PORT = 2910
    server_address = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.sendto(message.encode(), server_address)
        data, _ = sock.recvfrom(1024)
        print(f"Odpowiedź serwera: {data.decode()}")

    except socket.error as e:
        print(f"Błąd gniazda: {e}")

    finally:
        sock.close()

#ZAD14
def process_tcp_segment(tcp_segment):
    data_bytes = tcp_segment.replace('\n', ' ').split()

    source_port_hex = get_bytes(data_bytes, 2, 0)
    destination_port_hex = get_bytes(data_bytes, 2, 2)

    source_port = hex_to_dec("".join(source_port_hex))
    destination_port = hex_to_dec("".join(destination_port_hex))

    data_hex = data_bytes[32:]  # za opcjami
    data_ascii = hex_to_ascii("".join(data_hex))

    message = f"zad13odp;src;{source_port};dst;{destination_port};data;{data_ascii}"
    print("Wiadomość do wysłania:", message)

    #HOST = "212.182.24.27"
    HOST = "127.0.0.1"
    PORT = 2909
    server_address = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.sendto(message.encode(), server_address)
        data, _ = sock.recvfrom(1024)
        print(f"Odpowiedź serwera: {data.decode()}")
    except socket.error as e:
        print(f"Błąd gniazda: {e}")
    finally:
        sock.close()

#ZAD15
def process_ip_datagram(datagram):
    data_bytes = datagram.replace('\n', ' ').split()

    version = hex_to_dec(get_bytes(data_bytes, 1, 0)[0]) >> 4

    source_ip_hex = get_bytes(data_bytes, 4, 12)
    destination_ip_hex = get_bytes(data_bytes, 4, 16)

    source_ip = ".".join(str(hex_to_dec(b)) for b in source_ip_hex)
    destination_ip = ".".join(str(hex_to_dec(b)) for b in destination_ip_hex)

    protocol_type = hex_to_dec(get_bytes(data_bytes, 1, 9)[0])

    message_a = f"zad15odpA;ver;{version};srcip;{source_ip};dstip;{destination_ip};type;{protocol_type}"
    print("Wiadomość A:", message_a)

    #HOST = "212.182.24.27"
    HOST = "127.0.0.1"
    PORT = 2911
    server_address = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.sendto(message_a.encode(), server_address)
        data, _ = sock.recvfrom(1024)
        response = data.decode()
        print("Odpowiedź serwera A:", response)

        if response == "TAK":
            source_port = hex_to_dec("".join(get_bytes(data_bytes, 2, 20)))
            destination_port = hex_to_dec("".join(get_bytes(data_bytes, 2, 22)))

            data_hex = data_bytes[52:]
            data_ascii = hex_to_ascii("".join(data_hex))

            message_b = f"zad15odpB;srcport;{source_port};dstport;{destination_port};data;{data_ascii}"
            print("Wiadomość B:", message_b)

            sock.sendto(message_b.encode(), server_address)
            final_response, _ = sock.recvfrom(1024)
            print("Odpowiedź serwera B:", final_response.decode())

    except socket.error as e:
        print("Błąd socketu:", e)
    finally:
        sock.close()

if __name__ == "__main__":
    #process_udp_datagram(udp_datagram)
    #process_tcp_segment(tcp_segment)
    process_ip_datagram(ip_packet)

