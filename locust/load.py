import os
import json
from locust import HttpUser, task, between

# Read environment variables for wait time, request type, request body, query parameters, and headers
min_wait = float(os.getenv('LOCUST_MIN_WAIT', '1'))
max_wait = float(os.getenv('LOCUST_MAX_WAIT', '3'))
req_type = os.getenv('REQ_TYPE', 'GET')
req_body = os.getenv('REQ_BODY', '')
query_params = os.getenv('QUERY_PARAMS', '')
headers = json.loads(os.getenv('LOCUST_HEADERS', '{}'))

class MyUser(HttpUser):
    wait_time = between(min_wait, max_wait)

    @task
    def my_task(self):
        # Check the request type and perform the corresponding request
        if req_type.upper() == 'GET':
            self.client.get("/", params=query_params, headers=headers)
        elif req_type.upper() == 'POST':
            self.client.post("/", json=req_body, headers=headers)
        elif req_type.upper() == 'PUT':
            self.client.put("/", json=req_body, headers=headers)
        elif req_type.upper() == 'DELETE':
            self.client.delete("/", json=req_body, headers=headers)
