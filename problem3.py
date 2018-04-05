"""
Created on Fri Mar 16 23:27:24 2018
@author: patricio

For Solving Problem 3 in Project Euler.
"""

import time
import math


def find_prime_factors(n):
    p_list = []
    k = 1
    num = 2
    lim = int(math.sqrt(n)) + 1
    while num <= lim:
        if n % num == 0:
            p_list.append(num)
        while n % num == 0:
            n = n // num
        num = 2*k + 1
        k += 1
    return p_list


start = time.time()
print(max(find_prime_factors(600851475143)))
print(time.time() - start)