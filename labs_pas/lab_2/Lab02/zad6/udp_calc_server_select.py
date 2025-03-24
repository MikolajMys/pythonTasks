#!/usr/bin/env python

import socket
import sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2902

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print("[%s] UDP Calc Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))

try:
    while True:
        data, address = sock.recvfrom(4096)
        message_parts = data.decode().split()

        if len(message_parts) == 3:
            num1, op, num2 = message_parts
            print("[%s] Got from client %s ... : %s %s %s" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), str(address), num1, op, num2))

            try:
                # Obliczenia na podstawie operatora
                if op == '+':
                    result = float(num1) + float(num2)
                elif op == '-':
                    result = float(num1) - float(num2)
                elif op == '*':
                    result = float(num1) * float(num2)
                elif op == '/':
                    result = float(num1) / float(num2)
                else:
                    result = "Bad operator. I support only +, -, *, / math operators"

                sent = sock.sendto(str(result).encode(), address)

            except ValueError as e:
                result = "%s" % e
                sent = sock.sendto(str(result).encode(), address)

            except Exception as e:
                result = "Error: %s" % e
                sent = sock.sendto(str(result).encode(), address)

finally:
    sock.close()
