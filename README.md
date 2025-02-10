# Load Balancer

## Project Overview
This project implements a **Load Balancer** that distributes incoming client requests across multiple backend servers. The goal is to **balance the load efficiently** using different strategies such as:
- **Round-Robin** (equal distribution)
- **Least Connections** (prioritize the server with the lowest load)
- **Weighted Load Balancing** (optional: distribute based on server capacity)

The Load Balancer ensures **high availability, fault tolerance, and scalability** in a distributed system.

## Features
✅ Supports **multiple backend servers**  
✅ Implements **Round-Robin & Least Connections algorithms**  
✅ **Fault-tolerant**: Automatically detects and removes **offline servers**  
✅ **Multi-threading**: Handles multiple client requests at once  
✅ **Scalability**: Dynamically adds/removes backend servers (optional)  
✅ **Logging**: Tracks requests and performance metrics  

## Technologies Used
- **Python 3 / Java** (Choose your preferred language)
- **Sockets (TCP/IP)** for client-server communication
- **Multi-threading** for handling concurrent connections
- **Logging & Monitoring** for debugging and performance tracking

## Setup Instructions

### Prerequisites
- Install Python 3 (`sudo apt install python3` or `brew install python3`)
- Install Git (`sudo apt install git`)
- Clone the repository:
  ```sh
  git clone git@github.com:kianis4/load-balancer.git
  cd load-balancer
  ```

### Running the Load Balancer
1. **Start the backend servers**:
   ```sh
   python3 server.py
   ```
2. **Run the Load Balancer**:
   ```sh
   python3 load_balancer.py
   ```
3. **Start a client to send requests**:
   ```sh
   python3 client.py
   ```

## Contribution
1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a Pull Request (PR) with a clear description.

## License
MIT License
