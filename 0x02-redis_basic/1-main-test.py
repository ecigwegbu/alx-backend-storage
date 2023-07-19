#!/usr/bin/env python3
''' test file - task 1'''
Cache = __import__('exercise').Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    "bar": lambda d: d.decode("utf-8"),
    123: float
}

# key = cache.store(123)
# print('key: ', key, 'value: ', 123)
# val = cache.get(key, lambda d: d.decode("utf-8"))
# print(5)
# print('val:', val)
# exit(98)
print('key      ::     get()          <>     value   ')
for value, fnn in TEST_CASES.items():
    key = cache.store(value)
    val1 = cache.get(key, fn=fnn)
    print(key, "::", val1, " <> ", value)
    # assert cache.get(key, fn=fnn) == value
    assert val1  == value
    print('ASSERT OK.')
