import socket
import threading
import time

# List of backend servers
SERVERS = [("127.0.0.1", 9001), ("127.0.0.1", 9002), ("127.0.0.1", 9003)]
server_connections = {server: 0 for server in SERVERS}  # Track active connections
active_servers = SERVERS.copy()  # Maintain a list of active servers
lock = threading.Lock()  # Ensure thread-safe updates

def get_least_busy_server():
    """Returns the backend server with the fewest active connections."""
    with lock:
        if active_servers:
            return min(active_servers, key=server_connections.get)
        else:
            return None  # No available servers

def health_check():
    """Periodically checks if backend servers are online and updates active servers list."""
    global active_servers
    while True:
        print("🔍 Running Health Check...")  # Debugging statement
        with lock:
            for server in SERVERS:
                try:
                    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    test_socket.settimeout(1)  # Short timeout for quick check
                    test_socket.connect(server)
                    test_socket.close()

                    if server not in active_servers:
                        active_servers.append(server)  # Restore the server if it was down
                        print(f"✅ Server {server} is back online!")

                except (socket.timeout, ConnectionRefusedError):
                    if server in active_servers:
                        active_servers.remove(server)  # Remove the failed server
                        print(f"❌ Server {server} is down!")

        time.sleep(5)  # Check servers every 5 seconds



def handle_client(client_socket):
    """Handles client requests by forwarding to the least busy backend server."""
    backend_server = get_least_busy_server()
    
    if backend_server is None:
        print("⚠️ No available servers!")
        client_socket.send("503 Service Unavailable".encode())
        client_socket.close()
        return

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

    print(f"🚀 Load Balancer running on port {port} (Fault-Tolerant Mode)")

    # Start the health check thread
    threading.Thread(target=health_check, daemon=True).start()

    while True:
        client_socket, client_addr = lb_socket.accept()
        print(f"🔗 Connection from {client_addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_load_balancer()


