import socket

HOST = "127.0.0.1"
PORT = 13

server_address = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    num1 = input("Podaj pierwszą liczbę: ")
    sock.sendto(num1.encode(), server_address)

    op = input("Podaj operator: ")
    sock.sendto(op.encode(), server_address)

    num2 = input("Podaj drugą liczbę: ")
    sock.sendto(num2.encode(), server_address)

    data = sock.recv(1024).decode()
    print(f"Odpowiedź serwera: {data}")

except socket.error as e:
    print(f"Błąd: {e}")

sock.close()