import requests

for i in range(105):
    response = requests.get('http://127.0.0.1:8000/')
    print(f"Request {i+1}: Status {response.status_code}, Remaining {response.headers.get('X-RateLimit-Remaining')}")