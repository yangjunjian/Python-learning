#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""a test script of mydict which inherited from dict class"""
__author__ = 'Jason Yang'


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise
    
    def __setattr__(self, key, value):
        self[key] = value
