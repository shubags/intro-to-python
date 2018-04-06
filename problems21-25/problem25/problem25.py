#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 12:50:25 2018

@author: jeff
"""

def fibo(number):
    a, b = 0, 1
    status = True
    counter = 0
    
    while status:
#        print ('counter', counter)
        a, b = b, a + b
#        print ('a:', a)
        counter += 1
        
        if len(str(a)) == number:
            
            return counter
            status = False
            break

fibo(1000)