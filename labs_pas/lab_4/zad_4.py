import socket

def udp_math_server():
    HOST = "127.0.0.1"
    PORT = 13

    server_address = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    print(f"Serwer UDP nasłuchuje na {HOST}:{PORT} (kalkulator)")

    while True:
        try:
            # Odbierz pierwszą liczbę
            num1, client_address = sock.recvfrom(1024)
            num1 = num1.decode()
            print(f"Otrzymano pierwszą liczbę: {num1}")

            # Odbierz operator
            operator, _ = sock.recvfrom(1024)
            operator = operator.decode()
            print(f"Otrzymano operator: {operator}")

            # Odbierz drugą liczbę
            num2, _ = sock.recvfrom(1024)
            num2 = num2.decode()
            print(f"Otrzymano drugą liczbę: {num2}")

            # Wykonaj obliczenie
            try:
                n1 = float(num1)
                n2 = float(num2)

                if operator == '+':
                    result = n1 + n2
                elif operator == '-':
                    result = n1 - n2
                elif operator == '*':
                    result = n1 * n2
                elif operator == '/':
                    if n2 != 0:
                        result = n1 / n2
                    else:
                        result = "Błąd: Dzielenie przez zero"
                else:
                    result = "Błąd: Nieznany operator"

            except ValueError:
                result = "Błąd: Nieprawidłowe liczby"

            # Odeślij wynik
            result_str = str(result)
            sock.sendto(result_str.encode(), client_address)

        except Exception as e:
            print(f"Błąd: {e}")

if __name__ == "__main__":
    udp_math_server()
