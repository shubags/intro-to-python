#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 13:59:05 2018

@author: jeff
"""

def power_digit_sum(user_input):
    
    num_string = str(2 ** user_input)
    
    sum_of_digits = 0
    
    for digit in num_string:
        
        sum_of_digits += int(digit)
        
    return sum_of_digits

power_digit_sum(1000)