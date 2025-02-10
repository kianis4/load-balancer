import socket

def start_server(port):
    """Starts a simple TCP server that listens for client requests and responds."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Avoid "Address already in use" errors
    server_socket.bind(("0.0.0.0", port))  # Listen on all network interfaces
    server_socket.listen(5)

    print(f"✅ Server started on port {port}, waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"🔗 Connection from {addr}")

        try:
            request = client_socket.recv(1024).decode().strip()
            if request:
                print(f"📩 Received: {request}")

                response = f"Hello from Server {port}!"
                client_socket.sendall(response.encode())  # Ensure full message is sent
            else:
                print("⚠️ Received an empty request!")

        except Exception as e:
            print(f"⚠️ Error handling request: {e}")

        finally:
            client_socket.close()

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9001  # Default port 9001
    start_server(port)

