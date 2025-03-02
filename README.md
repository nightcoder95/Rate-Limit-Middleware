# Rate Limiting Middleware

## How It Works
- Tracks requests by IP using Django’s cache.
- Rolling window: Stores timestamps in a list, keeps only the last 5 minutes (300 seconds).
- Blocks IPs after 100 requests with a 429 response.
- Adds headers showing remaining requests.

## How to Test Locally
If the project folder is downloaded and used, Activate the virtual env included in the project folder
   ` midENV\Scripts\activate.bat`
    or
1. Install Django: `pip install django`
2. Run: `python manage.py runserver`
3. Use this script to test:

On the Terminal
`pip install requests` 
`python test_requests.py`


or

import requests
for i in range(105):
    r = requests.get('http://127.0.0.1:8000/')
    print(f"Request {i+1}: {r.status_code}, {r.headers.get('X-Rate-Limit-Remaining')}")


- **Thread Safety Note**: The current version uses Django’s default cache, which may not be fully thread-safe under heavy load. For production, we can consider a lock or atomic cache operations (e.g., Redis).