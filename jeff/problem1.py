#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:08:16 2018

@author: jeff
"""

#problem 1
#explicit
def multiples_of_3_or_5(number, method='explicit'):
    
    if method == 'explicit':
        total = 0
        for i in range(number):
            if (i % 3 == 0 or i % 5 == 0):
                total += i
    
    elif method == 'comprehension':
        total = sum([i for i in range(number) if (i % 3 == 0 or i % 5 == 0)])

    return total

multiples_of_3_or_5(1000,'explicit')
