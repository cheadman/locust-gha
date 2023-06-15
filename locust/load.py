import os
from locust import HttpUser, task, between

min_wait = float(os.getenv('LOCUST_MIN_WAIT', '1'))
max_wait = float(os.getenv('LOCUST_MAX_WAIT', '3'))
print(min_wait)
print(max_wait)

class MyUser(HttpUser):
    wait_time = between(min_wait, max_wait)

    @task
    def my_task(self):
        self.client.get("/")
