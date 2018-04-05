"""
Created on Fri Mar 16 22:24:40 2018
@author: patricio

Description:
This function calculates the sum of all multiples of 3 or 5 for a N number
of numbers
"""


def sum_if_mult_3_5(num_nums):
    sum_result = sum([i for i in range(num_nums) if i % 3 == 0 or i % 5 == 0])
    return sum_result


print(sum_if_mult_3_5(1000))

