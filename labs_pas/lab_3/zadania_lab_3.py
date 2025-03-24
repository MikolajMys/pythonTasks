import socket

def process_udp_datagram():
    hex_data = [
        0xed, 0x74, 0x0b, 0x55, 0x00, 0x24, 0xef, 0xfd, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61,
        0x6d, 0x6d, 0x69, 0x6e, 0x67, 0x20, 0x69, 0x6e, 0x20, 0x70, 0x79, 0x74, 0x68, 0x6f,
        0x6e, 0x20, 0x69, 0x73, 0x20, 0x66, 0x75, 0x6e
    ]

    datagram = bytes(hex_data)

    src_port = int.from_bytes(datagram[:2], byteorder='big')
    dst_port = int.from_bytes(datagram[2:4], byteorder='big')

    data_length = int.from_bytes(datagram[4:6], byteorder='big')
    data = datagram[8:].decode('utf-8')

    result = f"zad14odp;src;{src_port};dst;{dst_port};data;{data}"
    server = ("212.182.24.27", 2910)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(result.encode(), server)
    response, _ = sock.recvfrom(1024)
    sock.close()

    print("Odpowiedź serwera:", response.decode())

if __name__ == "__main__":
    process_udp_datagram()
