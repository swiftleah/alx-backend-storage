#!/usr/bin/env python3
''' task 0 '''
import uuid
import redis
from typing import Union


class Cache:
    ''' objects for storing data in redis storage '''
    def __init__(self) -> None:
        ''' init method with private redis variable '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''generates random key usinguuid and stores data in Redis'''
        Randomkey = str(uuid.uuid4())
        self._redis.set(Randomkey, data)
        return Randomkey
