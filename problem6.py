"""
Created on Sun Mar 18 18:40:10 2018

@author: patricio
"""

def sum_squares_first_n_numbers(num_nums):
    total_sum = 0
    for i in range(1,num_nums+1):
        total_sum += i**2
    return total_sum

def squre_sum_first_n_numbers(num_nums):
    total_sum = 0
    for i in range(1,num_nums+1):
        total_sum += i
    return total_sum**2


    
print(squre_sum_first_n_numbers(100) - sum_squares_first_n_numbers(100))

