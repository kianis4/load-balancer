import socket
import threading
import time
import logging

# Configure logging
logging.basicConfig(
    filename="load_balancer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# List of backend servers
active_servers = []  # Dynamically discovered servers
server_connections = {}  # Track connections for dynamically detected servers
lock = threading.Lock()  # Ensure thread-safe updates


def get_least_busy_server():
    """Returns the backend server with the fewest active connections."""
    with lock:
        if active_servers:
            return min(active_servers, key=server_connections.get)
        else:
            return None  # No available servers


def health_check():
    """Continuously scans for backend servers and updates the active server list."""
    global active_servers, server_connections
    while True:
        logging.info("🔍 Running Health Check...")
        with lock:
            discovered_servers = []
            for port in range(9001, 9010):  # Scan ports 9001-9009 for active servers
                server = ("127.0.0.1", port)
                try:
                    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    test_socket.settimeout(1)
                    test_socket.connect(server)
                    test_socket.close()

                    discovered_servers.append(server)
                    if server not in server_connections:
                        server_connections[server] = 0  # Initialize connection count

                except (socket.timeout, ConnectionRefusedError):
                    pass  # Ignore inactive ports

            # Detect new servers
            for server in discovered_servers:
                if server not in active_servers:
                    print(f"✅ Server {server} detected and added!")  # NEW: Print to terminal
                    logging.info(f"✅ Server {server} detected and added!")

            # Detect removed servers
            for server in active_servers:
                if server not in discovered_servers:
                    print(f"❌ Server {server} removed from active servers!")  # NEW: Print to terminal
                    logging.warning(f"❌ Server {server} removed from active servers!")

            # Update active server list
            active_servers = discovered_servers
            print(f"📡 Active servers: {active_servers}")  # NEW: Print to terminal
            logging.info(f"📡 Active servers: {active_servers}")

        time.sleep(5)  # Run health check every 5 seconds




def handle_client(client_socket):
    """Handles client requests by forwarding to the least busy backend server and logs request details."""
    backend_server = get_least_busy_server()
    
    if backend_server is None:
        logging.error("⚠️ No available servers! Sending 503 Service Unavailable.")
        client_socket.send("503 Service Unavailable".encode())
        client_socket.close()
        return

    server_connections[backend_server] += 1  # Increment connection count
    start_time = time.time()  # Start tracking response time

    try:
        logging.info(f"🔀 Forwarding request to {backend_server} (Active Connections: {server_connections[backend_server]})")

        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect(backend_server)

        request = client_socket.recv(1024)
        backend_socket.send(request)

        response = backend_socket.recv(1024)
        client_socket.send(response)

        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)  # Convert to milliseconds
        logging.info(f"📩 Request processed by {backend_server} | Response Time: {response_time} ms")

    except Exception as e:
        logging.error(f"⚠️ Error handling request: {e}")
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


