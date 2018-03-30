#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:57:31 2018

@author: jeff
"""

# =============================================================================
#  The sum of the squares of the first ten natural numbers is,
# 
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers 
# and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum.
# 
# =============================================================================

def sum_of_squares(number):
    
    squares = 0
    sum_of_squares = 0
    
    for i in range(1,number+1):
        squares += i**2
        sum_of_squares += i

    
    return ((sum_of_squares **2) - squares)

sum_of_squares(100)