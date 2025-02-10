import socket

def send_request(port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", port))
    client_socket.send("Hello Server!".encode())

    response = client_socket.recv(1024).decode()
    print(f"📩 Response from server {port}: {response}")

    client_socket.close()

if __name__ == "__main__":
    send_request(9001)
