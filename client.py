import socket
import threading

def send_request():
    """Sends a request to the Load Balancer."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8000))  # Connect to Load Balancer
    client_socket.send("Hello Load Balancer!".encode())

    response = client_socket.recv(1024).decode()
    print(f"📩 Response from Load Balancer: {response}")

    client_socket.close()

if __name__ == "__main__":
    threads = []
    for _ in range(10):  # Simulate 10 simultaneous clients
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


