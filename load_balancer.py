import socket
import threading

# List of backend servers
SERVERS = [("127.0.0.1", 9001), ("127.0.0.1", 9002), ("127.0.0.1", 9003)]
server_connections = {server: 0 for server in SERVERS}  # Track active connections

def get_least_busy_server():
    """Returns the backend server with the fewest active connections."""
    return min(server_connections, key=server_connections.get)

def handle_client(client_socket):
    """Handles client requests by forwarding to the least busy backend server."""
    backend_server = get_least_busy_server()
    server_connections[backend_server] += 1  # Increment connection count

    try:
        print(f"🔀 Forwarding request to {backend_server} (Active Connections: {server_connections[backend_server]})")

        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect(backend_server)

        request = client_socket.recv(1024)
        backend_socket.send(request)

        response = backend_socket.recv(1024)
        client_socket.send(response)

    except Exception as e:
        print(f"⚠️ Error handling request: {e}")
    finally:
        client_socket.close()
        backend_socket.close()
        server_connections[backend_server] -= 1  # Decrement connection count

def start_load_balancer(port=8000):
    """Starts the Load Balancer."""
    lb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lb_socket.bind(("0.0.0.0", port))
    lb_socket.listen(5)

    print(f"🚀 Load Balancer running on port {port} (Least Connections Mode)")

    while True:
        client_socket, client_addr = lb_socket.accept()
        print(f"🔗 Connection from {client_addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_load_balancer()

