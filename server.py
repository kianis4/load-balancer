import socket

def start_server(port):
    """Starts a simple TCP server that listens for client requests."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))  # Listen on all network interfaces
    server_socket.listen(5)

    print(f"✅ Server started on port {port}, waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"🔗 Connection from {addr}")
        request = client_socket.recv(1024).decode()
        print(f"📩 Received: {request}")

        response = f"Hello from Server {port}!"
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9001  # Default port 9001
    start_server(port)
