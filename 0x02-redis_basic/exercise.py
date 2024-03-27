#!/usr/bin/env python3
''' task 0 '''
import uuid
import redis
from typing import Callable, Union, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' counts number of times method is called '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' wrapper func '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' Decorator to store the history of inputs & outputs '''
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper decorator functionality """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> None:
    ''' replays history of func '''
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    ''' objects for storing data in redis storage '''
    def __init__(self) -> None:
        ''' init method with private redis variable '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''generates random key usinguuid and stores data in Redis'''
        Randomkey = str(uuid.uuid4())
        self._redis.set(Randomkey, data)
        return Randomkey

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        '''takes key str arg and arg fn'''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''takes str value from redis data storage'''
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        ''' gets int '''
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
