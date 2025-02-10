import socket
import itertools

# List of backend servers
SERVERS = [("127.0.0.1", 9001), ("127.0.0.1", 9002), ("127.0.0.1", 9003)]
server_cycle = itertools.cycle(SERVERS)  # Round-robin selection

def start_load_balancer(port=8000):
    """Starts the Load Balancer"""
    lb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lb_socket.bind(("0.0.0.0", port))
    lb_socket.listen(5)

    print(f"🚀 Load Balancer running on port {port}")

    while True:
        client_socket, client_addr = lb_socket.accept()
        print(f"🔗 Connection from {client_addr}")

        backend_server = next(server_cycle)  # Pick the next server (Round-Robin)
        print(f"🔀 Forwarding request to {backend_server}")

        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect(backend_server)

        request = client_socket.recv(1024)
        backend_socket.send(request)

        response = backend_socket.recv(1024)
        client_socket.send(response)

        client_socket.close()
        backend_socket.close()

if __name__ == "__main__":
    start_load_balancer()
