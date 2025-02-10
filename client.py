import socket

def send_request():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8000))  # Connect to Load Balancer
    client_socket.send("Hello Load Balancer!".encode())

    response = client_socket.recv(1024).decode()
    print(f"📩 Response from Load Balancer: {response}")

    client_socket.close()

if __name__ == "__main__":
    for _ in range(6):  # Send multiple requests
        send_request()

