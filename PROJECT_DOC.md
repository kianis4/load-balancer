Load Balancer Project Documentation
=====================================

I. Introduction
--------------

### Project Overview

This project implements a Load Balancer that efficiently distributes incoming client requests across multiple backend servers. The goal is to enhance system scalability, optimize resource utilization, and ensure high availability by routing traffic based on different load-balancing algorithms.

The Load Balancer is designed to:

* Distribute client requests across multiple backend servers to prevent overload.
* Ensure fault tolerance by detecting server failures and dynamically reassigning traffic.
* Improve performance through optimized request handling and monitoring.
* Provide real-time logging and analytics for better system observability.

### Motivation & Importance

Load balancing is a critical component in modern distributed systems, ensuring that no single server bears too much load, which can lead to performance degradation or system crashes. By implementing a load balancer, this project demonstrates key networking principles such as socket programming, concurrency, fault tolerance, and request distribution.

### Learning Outcomes

By completing this project, we gained insights into:

* ✅ **Networking & Sockets** – Understanding how client-server communication works.
* ✅ **Load Balancing Algorithms** – Implementing Round-Robin and Least Connections.
* ✅ **Fault Tolerance Mechanisms** – Detecting server failures and rerouting traffic dynamically.
* ✅ **Multi-threading** – Handling multiple concurrent connections efficiently.
* ✅ **Logging & Monitoring** – Recording system events, request flow, and response times.

II. Features of Application
---------------------------

### 1️⃣ Multi-Server Load Balancing

* ✅ **Round-Robin Algorithm** – Evenly distributes requests among all available servers.
* ✅ **Least Connections Algorithm** – Prioritizes sending requests to the server with the lowest active connections.

### 2️⃣ Fault Tolerance & Health Monitoring

* ✅ **Automated Server Health Checks** – The Load Balancer continuously monitors backend servers.
* ✅ **Failure Detection & Recovery** – If a server goes down, traffic is automatically rerouted to active servers.
* ✅ **Dynamic Server Restoration** – When a failed server is back online, it is seamlessly reintegrated.

### 3️⃣ Logging & Monitoring

* ✅ **Logs All Requests & Responses** – Every incoming client request is tracked and logged.
* ✅ **Monitors Response Times** – Logs the time taken to process requests, aiding in performance analysis.
* ✅ **Records Server Failures & Recoveries** – All system events are stored in `load_balancer.log`.

### 4️⃣ Scalability & Concurrency

* ✅ **Multi-threading Support** – Can handle multiple client requests simultaneously.
* ✅ **Dynamic Backend Server Management** – Backend servers can be added or removed without stopping the Load Balancer.

### 5️⃣ Error Handling & Security

* ✅ **Handles Connection Errors Gracefully** – Prevents crashes due to broken connections or failed servers.
* ✅ **Prevents Overloading Servers** – Uses Least Connections to intelligently manage traffic.
* ✅ **Rejects Requests When No Servers Are Available** – Sends 503 Service Unavailable response if all servers fail