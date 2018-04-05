
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

def sum_if_mult_2(list_of_numbers):
    sum_result = sum([i for i in list_of_numbers if i%2==0])
    return sum_result

def compute_fibonacci_seq_not_exceed(max_num):
    fib_list = [1,2]
    while (fib_list[len(fib_list)-1] <  max_num):
            fib_next_term = fib_list[len(fib_list)-2] + fib_list[len(fib_list)-1]
            fib_list.append(fib_next_term)
    return fib_list

print(sum_if_mult_2(compute_fibonacci_seq_not_exceed(4000000)))

