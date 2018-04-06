#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:54:54 2018

@author: jeff
"""


def find_factors(number):
    
    list1 = []

    [list1.append(i) for i in range(1, number) if (number % i == 0)]
    
    r = sum([num for num in list1])
    
    return r
    

def amicable_numbers(number):
    
    amicable_list = []
    
    for i in range(1, number + 1):
#        print ("num is:", i)
        x = find_factors(i)
#        print ("x is:", x)
        y = find_factors(x)
#        print ("y is:", y)
        
        if y == i and y != x:
            amicable_list.append(i)
            
    return sum([num for num in amicable_list])

amicable_numbers(10000)