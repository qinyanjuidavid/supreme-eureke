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
