#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:42:59 2018

@author: jeff
"""

# =============================================================================
# first function takes a value and determines the number of numbers within the collatz sequence
# =============================================================================
def find_collatz_sequence(number):
    
    start = number
    chain_list = [start]
     
    start = True
    
    while start:
        
        last_item = chain_list[-1]
        
        if last_item % 2 != 0 and last_item != 1:
            odd = (3 * last_item)+ 1
            chain_list.append(odd)
#            print ("this is an odd",odd)
        
        elif last_item % 2 == 0:
            even = last_item / 2
            chain_list.append(even)
#            print ("this is an even",even)
            
        elif last_item == 1:
            return len(chain_list)
            start = False
            break

        
# =============================================================================
# this function takes the range of numbers inputted by the user and checks which number (within the range)
# has the greatest collatz sequence
# =============================================================================

def iterate_numbers(user_input):
    
    max_chain = 0
    max_num = 0
    
    for num in range(1,user_input):
        num_temp = find_collatz_sequence(num)
        if num_temp > max_chain:
            max_chain = num_temp
            max_num = num
    return max_num

iterate_numbers(1000000)