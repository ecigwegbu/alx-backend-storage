#!/usr/bin/env python3
"""5. Implement expiring web cache and tracker"""
import requests
import redis


def get_page_decorator(gt_page):
    def wrapper(url):
        gt_page(url)
        r = redis.Redis()
        count = r.incr("count:{url}")
        r.expire("count:{url}", 10)
    return wrapper


@get_page_decorator
def get_page(url: str) -> str:
    """Return the URL of a web page"""
    # url = "https://www.google.com"
    response = requests.get(url)
    print(response.text)
    return response.text


url = "https://www.google.com"
print(get_page(url))
r = redis.Redis()
print('Visited: ', int(r.get("count:{url}")))


if __name__ == '__main__':
    pass
