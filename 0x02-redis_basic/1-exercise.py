#!/usr/bin/env python3
"""0. Writing strings to Redis
Create a Cache class. In the __init__ method, store an instance of the
Redis client as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the
input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes,
int or float.
"""
import redis
from typing import Union, Callable, Any
from uuid import uuid4


class Cache:
    """Class for writing strings to Redis"""
    def __init__(self) -> None:
        """constructor for Cache Class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key, use it to fill a value in the
        database, and return a string"""
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Any:
        """Takes a key string argument and an optional Callable argument
        named fn. This callable will be used to convert the data back
        to the desired format."""
        if (key == "") or bool(self._redis.exists(key)) is False:
            return None
        if fn is None:
            return self._redis.get(key)
        if fn == int:
            return self.get_int(key)
        return self.get_str(key)

    def get_str(self, key: str) -> Any:
        """Automatically parametrize Cache.get with the correct
        conversion function"""
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> Any:
        """Automatically parametrize Cache.get with the
        correct conversion function"""
        return int(self._redis.get(key))


if __name__ == '__main__':
    pass
