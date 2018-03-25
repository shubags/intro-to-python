"""
Created on Thu Mar 22 12:16:03 2018
@author: patricio

sum_digits_num: recieves a number and compute the sum of it's digits
"""

def sum_digits_num(num):
    sum_digits = sum([int(digit) for digit in str(num)])
    return sum_digits

num = 2**1000

print(sum_digits_num(num))
