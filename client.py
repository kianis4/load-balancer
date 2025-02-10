import socket
import threading
import time

def send_request():
    """Sends a request to the Load Balancer and handles errors properly."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(2)  # Prevent hanging connections
        client_socket.connect(("127.0.0.1", 8000))  # Connect to Load Balancer
        time.sleep(0.5)  # Add small delay before sending

        client_socket.sendall("Hello Load Balancer!".encode())  # Ensure full message is sent

        response = client_socket.recv(1024).decode()
        print(f"📩 Response from Load Balancer: {response}")

    except ConnectionResetError:
        print("❌ Connection reset by the server.")
    except BrokenPipeError:
        print("⚠️ Broken pipe error. Server might have closed the connection.")
    except socket.timeout:
        print("⌛ Request timed out.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    threads = []
    for _ in range(10):  # Simulate 10 concurrent clients
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()
        time.sleep(0.1)  # Small delay between client requests

    for thread in threads:
        thread.join()



