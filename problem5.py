"""
Created on Sun Mar 18 10:34:22 2018
@author: patricio

is_divisible_by: given a number and a list of numbers, it returns true if the
number is divisible by all the numbers in the list or false if not.
"""
import time

def is_divisible_by(number, list_of_numbers):
    default = True
    for num in list_of_numbers:
        if number % num != 0:
            default = False
            break
    return default
    
start = time.time()    
    
num = 2520
condition_meet = False
lom = list(range(1,21))

while(condition_meet==False):
    if is_divisible_by(num, lom):
        condition_meet = True
    else:
        num += 2

print(num)

print(time.time()-start)
