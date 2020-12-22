#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2020-12-21')


log(now)()
print(now.__name__)

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2020-12-21')


log('execute')(now)()

print(now.__name__)
