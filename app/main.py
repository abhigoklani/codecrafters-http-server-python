import socket

def main():
    print("Starting server on port 4221...")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        conn, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        request = conn.recv(1024).decode("utf-8")
        print("Request received:\n", request)

        if request.startswith("GET / "):
            response = "HTTP/1.1 200 OK\r\n\r\n"
        else:
            response = "HTTP/1.1 404 Not Found\r\n\r\n"

        conn.sendall(response.encode("utf-8"))
        conn.close()

if __name__ == "__main__":
    main()
