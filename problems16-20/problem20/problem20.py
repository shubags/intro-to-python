#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:28:03 2018

@author: jeff
"""


def factorial_digit_sum(number):
    
    empty_list = []
    prod = 1
    running_sum = 0
    [empty_list.append(x) for x in range(1, number + 1)]
    
    for num in empty_list:
        prod *= num
    
    for item in str(prod):
        running_sum += int(item)
    
    return running_sum


factorial_digit_sum(100)
