import socket


def main():
    print("Starting TCP server on port 4221...")

    # Create a server socket bound to localhost:4221
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept()[0].send(b"HTTP/1.1 200 OK\r\n\r\n")
    server_socket.accept()  # wait for client
    server_socket.listen()
    print("Server listening on port 4221...")
    print("Logs from your program will appear here!")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 4221))
    server_socket.listen(1)

    client_socket, addr = server_socket.accept()

    # You can add minimal response or just close connection here
    client_socket.close()


    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Minimal HTTP 200 OK response
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Length: 0\r\n"
            "\r\n"
        )
        client_socket.sendall(response.encode())
        client_socket.close()


if __name__ == "__main__":
    main()
