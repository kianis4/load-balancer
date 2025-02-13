Load Balancer
================

Project Overview
---------------

This project implements a Load Balancer that efficiently distributes incoming client requests across multiple backend servers. The goal is to ensure high availability, scalability, and fault tolerance using different load-balancing strategies such as:

### Load Balancing Strategies

* **Round-Robin**: Equal distribution of requests across servers
* **Least Connections**: Routes traffic to the server with the fewest active connections
* **Fault Tolerance & Health Monitoring**: Automatically detects and removes failed servers, then reintegrates them when they recover
* **Logging & Monitoring**: Tracks request flow, server status, and response times

Features
--------

### Key Features

✅ **Multi-Server Support**: Balances traffic between multiple backend servers.
✅ **Multiple Load Balancing Algorithms**: Implements Round-Robin and Least Connections.
✅ **Fault Tolerance**: Continuously checks server health, removing and restoring servers as needed.
✅ **Multi-threading**: Efficiently handles multiple concurrent client connections.
✅ **Logging & Monitoring**: Tracks request distribution, response times, and server health in `load_balancer.log`.
✅ **Scalability**: Can dynamically add or remove backend servers.
✅ **Robust Error Handling**: Prevents crashes and connection issues with proper exception handling.

Technologies Used
-----------------

* **Python 3**: For backend development.
* **Sockets (TCP/IP)**: For communication between the Load Balancer, clients, and backend servers.
* **Multi-threading**: To handle concurrent client connections efficiently.
* **Logging Module**: For monitoring request flow, errors, and system behavior.

Project Structure
-----------------

* `client.py`: Simulates client requests to the Load Balancer
* `server.py`: Backend server responding to client requests
* `load_balancer.py`: Core Load Balancer implementation
* `PROJECT_STEPS.md`: Step-by-step project implementation guide
* `README.md`: Project overview and setup instructions
* `logging_test.log`: Log file for request handling and server health
* `fault_tolerance_test.log`: Log file verifying server failure handling
* `client_test.log`: Log file tracking client requests and responses
* `server_test.log`: Log file for backend server testing
* `venv/`: Virtual environment for package isolation

Setup Instructions
-----------------

### Prerequisites

* **Install Python 3**:
	+ `sudo apt install python3` (Ubuntu/Linux)
	+ `brew install python3` (macOS)
* **Install Git**:
	+ `sudo apt install git`
* **Clone the repository**:
	+ `git clone git@github.com:kianis4/load-balancer.git`
	+ `cd load-balancer`
* **Install dependencies (if any)**:
	+ `pip install -r requirements.txt`

### Running the Project

#### Start Backend Servers

Run multiple instances of backend servers on different ports:

```
python3 server.py 9001 &
python3 server.py 9002 &
python3 server.py 9003 &
```

#### Start the Load Balancer

```
python3 load_balancer.py
```

#### Run Client Requests

```
python3 client.py
```

### Testing & Monitoring

Check `load_balancer.log` for request distribution, response times, and server status:

```
cat load_balancer.log
```

Simulate a server failure by stopping a backend server:

```
pkill -f "server.py 9002"
```

Then check logs to confirm it was detected.

## Code Architecture

Below is a breakdown of each Python file in this project, showing how it interacts with the others:

### 1. server.py
• start_server(port): Creates a TCP socket, binds to the specified port, listens for connections, and sends a welcome response.  
• The server is designed to handle each request one at a time, creating short-lived connections with clients.  

When multiple servers (on different ports) are running, the Load Balancer will route incoming requests to them based on the chosen strategy.

### 2. load_balancer.py
• start_load_balancer(port=8000): Main entry to start listening for incoming connections from clients. For each new connection, a separate thread is spawned to handle traffic (handle_client) without blocking others.  
• handle_client(client_socket): Receives a request from the client, chooses the backend server (based on get_least_busy_server), forwards the request, and returns the server's response back to the client. Also performs logging and tracks how long each request takes.  
• get_least_busy_server(): Chooses the server with the fewest active connections in a thread-safe way.  
• health_check(): Runs in its own thread to periodically verify each backend server’s availability. If a server is down, it’s removed from the rotation; if it recovers, it’s added back in.

### 3. client.py
• send_request(): Opens a connection to the Load Balancer, sends a message, and prints out the server’s response.  
• This file is mainly used for testing and demonstration, simulating multiple concurrent clients using threads.  

Together, these components form a highly concurrent, fault-tolerant load balancing system. The client requests flow to the Load Balancer (load_balancer.py), which intelligently chooses an available server (server.py). Failing or recovering servers are managed by the health_check mechanism.

Contribution
------------

* **Fork the repository**.
* **Create a new branch for your feature**.
* **Submit a Pull Request (PR) with a clear description**.

License
-------

MIT License

