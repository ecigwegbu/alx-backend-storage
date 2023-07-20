#!/usr/bin/env python3
"""5. Implement expiring web cache and tracker"""
import requests
import redis
import typing


def get_page_decorator(get_page):
    def wrapper():
        gt_page()
        r = redis.Redis()
        count = r.incr("count:{url}")
        r.expire("count:{url}", 10)
    return wrapper


@get_page_decorator
def get_page(url: str) -> str:
    """Return the URL of a web page"""
    # url = "https://www.google.com"
    response = requests.get(url)
    return response.text


url = "https://www.google.com"
print(get_page(url))
r = redis.redis()
print('Visited: ', int(r.get("count:{url}")))


if __name__ == '__main__':
    pass
