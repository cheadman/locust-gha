import os
from locust import HttpUser, task, between

# Set the minimum and maximum wait times based on environment variables
min_wait = float(os.getenv('LOCUST_MIN_WAIT', '1'))
max_wait = float(os.getenv('LOCUST_MAX_WAIT', '3'))

# Define the payload data, a list of objects
payload_data = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "Alice"}
]

# Generator function to yield the next object from the payload_data list
def payload_generator():
    index = 0
    while True:
        yield payload_data[index]
        index = (index + 1) % len(payload_data)

payload_gen = payload_generator()

class MyUser(HttpUser):
    wait_time = between(min_wait, max_wait)

    @task
    def my_task(self):
        # Perform a GET request to "/"
        self.client.get("/")
        self.wait()

        # Get the next object from the payload generator
        payload = next(payload_gen)

        # Perform a POST request to "/endpoint" with the payload as JSON
        self.client.post("/endpoint", json=payload)
        self.wait()

        # Perform a PUT request to "/endpoint"
        self.client.put("/endpoint", json=payload)
