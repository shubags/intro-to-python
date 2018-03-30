#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:42:51 2018

@author: jeff
"""

def fibonacci_sequence(number, method = 'explicit'):
    if method == 'explicit':
        a, b = 1, 1
        total = 0
        while a <= number:
            if a % 2 == 0:
                total += a
            a, b = b, a + b
        return total
    
fibonacci_sequence(4000000)