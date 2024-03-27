#!/usr/bin/env python3
''' obtains HTML content of particular URL and returns it'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_ = redis.Redis()


def get_content(method: Callable) -> Callable:
    '''caches fetched data'''
    @wraps(method)
    def invoker(url) -> str:
        ''' func'''
        redis_.incr(f'count:{url}')
        result = redis_.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_.set(f'count:{url}', 0)
        redis_.setex(f'result:{url}', 10, result)
        return result
    return invoker


@get_content
def get_html(url: str) -> str:
    '''gets content from url'''
    return requests.get(url).text
