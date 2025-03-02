# Rate Limiting Middleware

## How It Works
- Tracks requests by IP using Django’s cache.
- Rolling window: Stores timestamps in a list, keeps only the last 5 minutes (300 seconds).
- Blocks with a 429 status and custom template after 100 requests.
- Adds headers showing remaining requests.

## How to Test Locally
## How to Test Locally
1. Install: `pip install django`
2. Run: `python manage.py runserver`
3. Test: `python test_requests.py` (sends 105 requests, expect 429 after 100).


- **Thread Safety Note**: The current version uses Django’s default cache, which may not be fully thread-safe under heavy load. For production, we can consider a lock or atomic cache operations (e.g., Redis).