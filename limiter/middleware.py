from django.core.cache import cache
from django.http import HttpResponse
import time

class CustomRateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get IP address from the request
        ip = request.META.get('REMOTE_ADDR')
        
        # We need to get the list of timestamps of this IP from the cache, if empty, return an empty list
        request_times = cache.get(ip, default=[])
        
        current_time = time.time()
        
        five_minute_ago = current_time - 300
        # Filter only the requests that happened in the last 5 minutes
        request_times = [timestamp for timestamp in request_times if timestamp > five_minute_ago]
        
        # Check whether the current request exceed the threshold(100 requests in 5 minutes)
        if len(request_times)>=100:
            return HttpResponse("Too many requests", status=429)
        
        # After checking the request whether its under 100, Add the current request time to the list
        request_times.append(current_time)
        # Save to the list back to cache, expires after 5 minutes.
        cache.set(ip, request_times, timeout=300)
        
        
        response = self.get_response(request)
        
        # Adding custom headers to show the how many responses are left
        remaining_requests = 100 - len(request_times)
        response['X-RateLimit-Remaining'] = str(remaining_requests)
        
        return response
        