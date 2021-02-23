#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test script of subprocess"""
__author__ = 'Jason Yang'

import subprocess

print('$ nslookup www.python.org')
r = subprocess.run(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output)
print('Exit code:', p.returncode)
