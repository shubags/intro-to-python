
"""
Created on Fri Mar 16 22:40:36 2018
@author: patricio

Description:
Script used to solve Problem 2 in Project Euler.
Two functions were defined in order to find solution.

1) sum_if_mult_2: Given a list of numbers this function computes the sum
    of the numbers in the list that are even.
    
2) compute_fibonacci_seq_not_exceed: Computes the terms in the fibonbacci sequence 
    whose value doesn't exceed the max_num paremeter

"""

from lib import utilities as utl


def compute_fibonacci_seq_not_exceed(max_num):
    fib_list = [1,2]
    fib_next_term = 0
    while fib_next_term < max_num:
            fib_next_term = fib_list[len(fib_list)-2] + fib_list[len(fib_list)-1]
            fib_list.append(fib_next_term)
    return fib_list


print(utl.sum_if_mult(compute_fibonacci_seq_not_exceed(4000000), 2))

