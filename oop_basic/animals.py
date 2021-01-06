#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of class"""
__author__ = 'Jason Yang'


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
d = Dog()
c = Cat()

run_twice(a)
run_twice(d)
run_twice(c)

print('a is Animal?', isinstance(a, Animal))
print('d is Dog?', isinstance(d, Dog))
print('c is Cat?', isinstance(c, Cat))

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))
