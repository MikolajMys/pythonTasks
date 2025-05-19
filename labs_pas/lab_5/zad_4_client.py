import socket
import time

HOST = "127.0.0.1"
PORT = 2914

server_address = (HOST, PORT)
message = b"Test message"

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Rozpoczynanie testu UDP...")

start_udp = time.time()

for _ in range(100):
    udp_sock.sendto(message, server_address)
    data, _ = udp_sock.recvfrom(1024)

end_udp = time.time()
udp_duration = end_udp - start_udp

udp_sock.close()
print(f"Czas transmisji UDP: {udp_duration:.6f} sekund")

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect(server_address)

print("Rozpoczynanie testu TCP...")

start_tcp = time.time()

for _ in range(100):
    tcp_sock.sendall(message)
    data = tcp_sock.recv(1024)

end_tcp = time.time()
tcp_duration = end_tcp - start_tcp

tcp_sock.close()
print(f"Czas transmisji TCP: {tcp_duration:.6f} sekund")

print("\nPorównanie wyników:")

if udp_duration < tcp_duration:
    print("UDP było szybsze.")
else:
    print("TCP było szybsze.")

print(f"Różnica czasu: {abs(udp_duration - tcp_duration):.6f} sekund")
