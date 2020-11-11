#!/usr/bin/env python
# encoding: utf-8
# @Author: sunyabo
# @Date: 2020/11/11 上午9:15
import functools
import sys
from time import time, sleep
import logging as logger

logger.basicConfig(stream=sys.stdout, level=logger.DEBUG)


def log(func):
    def wrapper(*args, **kwargs):
        logger.info("call {}".format(func.__name__), )
        return func(*args, **kwargs)

    return wrapper


@log
def now(*args, **kwargs):
    print(time())


def logger(logger_level):
    """设计一个decorator，可以作用于任何函数上，并打印该函数的执行时间"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            r = func(*args, **kwargs)
            print("call {} cost {} ms".format(func.__name__, 1000 * (time() - start_time)))
            return r

        return wrapper

    return decorator


@logger("DEBUG")
def func(a, b):
    sleep(2)
    return a + b


@logger("DEBUG")
def func1(num):
    count = 0
    for i in range(num):
        count = count + num
    return count


if __name__ == '__main__':
    # func(1, 2)
    func1(100000000)
