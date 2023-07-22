#!/usr/bin/env python3
"""5. Implement expiring web cache and tracker"""
import redis
import time

def record_visit(redis_conn, website):
    # Key for storing the visit timestamps
    key = f"visits:{website}"

    # Add the current timestamp to the list
    redis_conn.lpush(key, time.time())

    # Trim the list to keep only the last 10 timestamps
    redis_conn.ltrim(key, 0, 9)

if __name__ == "__main__":
    # Connect to the Redis server
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Simulate visiting the website once every second for 10 seconds
    website_to_visit = "example.com"
    for _ in range(10):
        record_visit(r, website_to_visit)
        time.sleep(1)

    # Wait for 3 seconds without visiting the website
    time.sleep(3)

    # Get the visit count by getting the length of the list
    visit_count = r.llen(f"visits:{website_to_visit}")
    print(f"Visits for {website_to_visit}: {visit_count}")
