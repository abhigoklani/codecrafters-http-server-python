import socket

def main():
    print("Logs from your program will appear here!")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 4221))
    server_socket.listen(1)

    while True:
        client_connection, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_connection.close()

if __name__ == "__main__":
    main()
