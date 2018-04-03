#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 09:07:46 2018

@author: jeff
"""
# =============================================================================
# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# =============================================================================

#this function goes through every possible pythagorean combinations (or steps) for numbers from zero to the input (1000)
#after setting a, b, and c as possible combinations, it checks whether the two pythagorean parameters (square and sum) equal the input (1000)

def find_pythagorean_trips(number):
    for a in range (1 , number):
        for b in range (a + 1 , number):
            c = number - a - b
            if (a ** 2 + b ** 2 == c ** 2) & (a + b + c == number):
                print (a, b, c)
                print (a * b * c)
                break

find_pythagorean_trips(1000)