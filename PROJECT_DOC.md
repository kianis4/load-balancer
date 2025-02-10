Load Balancer Project Documentation
=====================================

Project Overview
---------------

This project implements a Load Balancer in Python that distributes incoming client requests across multiple backend servers. The goal is to efficiently balance the load, ensure high availability, and optimize resource utilization using various load-balancing techniques.

Features
--------

### Round-Robin Load Balancing

Distributes requests sequentially across backend servers.

### Least Connections Algorithm

Directs requests to the server with the fewest active connections.

### Fault Tolerance

Automatically detects server failures and reroutes traffic.

### Dynamic Scaling

Allows adding or removing servers dynamically.

### Multi-threading

Handles multiple concurrent client requests.

### Logging and Monitoring

Tracks request distribution and server performance.

Technologies Used
----------------

### Python 3

### Sockets (TCP/IP) for Networking

### Multi-threading for Concurrent Connections

### Logging for Monitoring and Debugging

Project Setup
-------------

### Prerequisites

* Install Python 3:
  ```sh
  sudo apt install python3  # Ubuntu/Linux
  brew install python3  # macOS
  ```
* Install Git (for version control):
  ```sh
  sudo apt install git
  ```
* Clone the repository:
  ```sh
  git clone git@github.com:kianis4/load-balancer.git
  cd load-balancer
  ```
* Install required dependencies (if any):
  ```sh
  pip install -r requirements.txt
  ```

System Architecture
-----------------

The system consists of three main components:

### Clients

Send requests to the Load Balancer.

### Load Balancer

Directs client requests to an available backend server based on the chosen algorithm.

### Backend Servers

Process client requests and return responses.

Implementation Steps
--------------------

### Phase 1: Setup & Research

* Research Load Balancers and socket programming.
* Set up the development environment and create project files.

### Phase 2: Backend Server Implementation

* Implement a simple TCP server (server.py) that listens for client requests.
* Run multiple backend server instances on different ports.

### Phase 3: Load Balancer Implementation

* Create a Load Balancer (load_balancer.py) that listens for client requests.
* Implement Round-Robin Load Balancing.
* Implement Least Connections Algorithm.

### Phase 4: Enhancements & Fault Tolerance

* Implement a health check mechanism to detect server failures.
* Allow dynamic scaling (adding/removing backend servers).
* Implement logging and monitoring.

### Phase 5: Testing & Performance Optimization

* Create a test client (client.py) to send requests.
* Measure response times under different traffic loads.
* Optimize request handling efficiency.

### Phase 6: Documentation & Finalization

* Write the project report.
* Create presentation slides.
* Record a demo video (optional).

Running the Project
-------------------

### Start Backend Servers

```sh
python3 server.py 9001 &
python3 server.py 9002 &
python3 server.py 9003 &
```

### Start Load Balancer

```sh
python3 load_balancer.py
```

### Run Client Requests

```sh
python3 client.py
```

Future Enhancements
-------------------

### Weighted Load Balancing

Distribute requests based on server capacity.

### HTTPS Support

Secure communication using TLS.

### Web Interface

Monitor request distribution visually.

### Machine Learning Optimization

Predict traffic patterns and allocate resources dynamically.

Conclusion
----------

This project successfully implements a Load Balancer in Python to manage incoming client requests efficiently. By using multi-threading, fault tolerance, and dynamic scaling, the system ensures high availability and optimized resource utilization.