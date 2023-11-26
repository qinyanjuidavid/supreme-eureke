# supreme-eureke
## SECTION A
### 1. Give examples of different integration protocols you have come across and give example scripts in python 3 on how to achieve each one. (10 pts)
#### 1. RESTful API
RESTful APIs are widely used for communication between systems. They are based on standard HTTP methods (GET, POST, PUT, PATCH and DELETE) and often use JSON for data exchange.

**Example Python Script:**
```python
import requests

# Define API endpoint
url = "https://api.example.com/users"

# Example GET request
response = requests.get(url)
print("GET Response:", response.json())

# Example POST request
new_user = {"username": "john_doe", "email": "john.doe@example.com"}
post_response = requests.post(url, json=new_user)
print("POST Response:", post_response.json())
```

#### 2. GraphQL
GraphQL is a query language for APIs that allows clients to request only the data they need. It provides a more flexible and efficient alternative to traditional REST APIs.
**Example Python Script:**
```python
import requests

# Define GraphQL endpoint
url = "https://api.example.com/graphql"

# Example GraphQL query
query = """
    query {
        user(id: 1) {
            id
            username
            email
        }
    }
"""

# Send GraphQL query
response = requests.post(url, json={"query": query})
print("GraphQL Response:", response.json())
```

### 2. Give a walkthrough of how you will manage a data streaming application sending one million notifications every hour while giving examples of technologies and configurations you will use to manage load and asynchronous services. (10 pts)
- Effectively managing a data streaming application that sends one million notifications every hour demands a strategic approach. In this walkthrough, I'll outline the key strategies and technologies I would employ to manage the load efficiently and ensure seamless asynchronous service processing.

### Technologies
#### 1. Apache Kafka for Data Streaming
- For robust data streaming, Apache Kafka is the chosen tool. Its selection is rooted in its unparalleled scalability, fault tolerance, and support for real-time event processing. Kafka's distributed architecture ensures high throughput and low latency, making it an ideal choice for handling the substantial load of one million notifications per hour.
#### 2. Redis for Caching
- Caching, a critical aspect of performance optimization, is entrusted to Redis. Redis stands out for its exceptional speed and versatility as an in-memory data store. Its ability to handle frequently accessed data efficiently aligns with the goal of improving data retrieval speed for our streaming application.
#### 3. Celery for Asynchronous Processing
- Asynchronous task handling is a key component of our strategy, and Celery is the chosen tool for this purpose. Celery's distributed architecture and support for various message brokers make it a robust solution for managing asynchronous tasks, ensuring optimal performance and reliability.

### Load Management Strategies
### 1. Horizontal Scaling
- To address the challenge of high load, horizontal scaling is implemented by deploying multiple instances of the application. Nginx is selected as the load balancer due to its versatility and ability to evenly distribute traffic among the instances.
### 2. Performance Monitoring
- Monitoring the system's performance is paramount for identifying bottlenecks and ensuring optimal operation. Prometheus and Grafana are chosen for their robust monitoring capabilities.
