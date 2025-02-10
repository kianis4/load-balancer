# Project Implementation Steps: Load Balancer

This document provides a **step-by-step** guide for implementing the Load Balancer project. Follow these steps sequentially.

---

## **Phase 1: Setup & Research**
### ✅ Step 1: Research Load Balancing
- Understand **Load Balancers** (Google search: "What is a Load Balancer?")
- Read about **Round-Robin and Least Connections algorithms**.
- Learn **Socket Programming** in Python or Java.
- Study **multi-threading** for handling multiple client connections.

### ✅ Step 2: Set Up Development Environment
- Install **Python 3** (`sudo apt install python3`)
- Install **Git** (`sudo apt install git`)
- Clone your repository:
  ```sh
  git clone git@github.com:kianis4/load-balancer.git
  cd load-balancer
  ```
- Install any required libraries (`pip install requirements.txt` if needed)

---

## **Phase 2: Implement Backend Servers**
### ✅ Step 3: Create a Simple Server
- Write `server.py`:
  - Listens for client requests.
  - Responds with `"Hello from Server X"`.
- Example (Python):
  ```python
  import socket

  HOST = "0.0.0.0"  # Listen on all IPs
  PORT = 9001  # Change for each server instance

  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((HOST, PORT))
  server_socket.listen(5)

  print(f"Server listening on {PORT}")

  while True:
      client_socket, addr = server_socket.accept()
      request = client_socket.recv(1024).decode()
      print(f"Received: {request}")
      client_socket.send(f"Hello from Server {PORT}".encode())
      client_socket.close()
  ```

### ✅ Step 4: Run Multiple Backend Servers
Start **3 different** servers on **ports 9001, 9002, and 9003**:
```sh
python3 server.py 9001 &
python3 server.py 9002 &
python3 server.py 9003 &
```

---

## **Phase 3: Implement Load Balancer**
### ✅ Step 5: Create Load Balancer Skeleton
- Write `load_balancer.py`:
  - Listens for client requests.
  - Forwards the request to a backend server.
  - Sends the response back to the client.

Example:
```python
import socket
import itertools

HOST = "0.0.0.0"
PORT = 8000
SERVERS = [("127.0.0.1", 9001), ("127.0.0.1", 9002), ("127.0.0.1", 9003)]
server_cycle = itertools.cycle(SERVERS)  # Round-Robin

lb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lb_socket.bind((HOST, PORT))
lb_socket.listen(5)

while True:
    client_socket, addr = lb_socket.accept()
    backend_server = next(server_cycle)  # Round-Robin
    backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    backend_socket.connect(backend_server)
    
    request = client_socket.recv(1024)
    backend_socket.send(request)
    response = backend_socket.recv(1024)
    
    client_socket.send(response)
    client_socket.close()
    backend_socket.close()
```

---

## **Phase 4: Add Load Balancing Algorithms & Logging**
### ✅ Step 6: Implement Least Connections Algorithm
Modify `load_balancer.py` to track active connections per server and send new requests to the **least busy server**.

Example:
```python
import socket
import threading

server_connections = {("127.0.0.1", 9001): 0, ("127.0.0.1", 9002): 0, ("127.0.0.1", 9003): 0}

def get_least_busy_server():
    return min(server_connections, key=server_connections.get)

while True:
    client_socket, addr = lb_socket.accept()
    backend_server = get_least_busy_server()
    server_connections[backend_server] += 1

    backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    backend_socket.connect(backend_server)
    threading.Thread(target=handle_request, args=(client_socket, backend_socket, backend_server)).start()
```

---

## **Final Phase: Report & Presentation**
- Write the **Project Report** (`report.md`).
- Create **PowerPoint slides** (`presentation.pptx`).
- Record a **Demo Video** (Optional).

---

🚀 **Congratulations! You’ve built a fully functional Load Balancer!**