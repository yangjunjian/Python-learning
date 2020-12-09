#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break


def _odd_iter():
    n = 3
    while True:
        yield n
        n = n + 2


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


if __name__ == '__main__':
    main()
