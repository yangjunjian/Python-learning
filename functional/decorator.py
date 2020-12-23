#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2020-12-22')


log(now)()
print(now.__name__)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2020-12-22')


log('execute')(now)()
print(now.__name__)


#   打印程序运行时间（或者在程序运行前后打印log）：日志需在wrapper函数内部打印


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t_begin = time.time()
        f_t = fn(*args, **kw)
        t_end = time.time()
        print('%s executed in %s ms.' % (fn.__name__, (t_end - t_begin)*1000))
        return f_t
    return wrapper


@metric
def prod():
    return reduce(lambda x, y: x * y, range(1, 10001))


metric(prod)()


@metric
def sum():
    return reduce(lambda x, y: x + y, range(1, 10000001))


metric(sum)()


def log(param):
    if callable(param):
        @functools.wraps(param)
        def wrapper(*args, **kw):
            print('begin call')
            f_t = param(*args, **kw)
            print('end call')
            return f_t
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin %s' % param)
                f_t = func(*args, **kw)
                print('end call')
                return f_t
            return wrapper
        return decorator


@log
def fun1():
    print('log no param!')


log(fun1)()


@log('execute')
def fun2():
    print('log with param!')
