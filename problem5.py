"""
Created on Sun Mar 18 10:34:22 2018
@author: patricio

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

Since not all numbers from 1 to 20 (lets call it k) are primes and those numbers can be
expressed as a product of prime numbers, our approach consists in first finding
all prime numbers below k and the exponents attached to each of the prime numbers
which can lead to produce any of the numbers between 1 and k. Then the product of
those numbers (exponent included) is the smallest number that we're looking.
For instance if k = 4 meaning that I want to find the smallest number divisible
by numbers 1 trhough 4, solution would be: 2*3*2 = 12. Noticing that 4 is implied
in the 2*2 multiplication. So in this case the exponent of 2 would be 2.

Getting back to the problem since for instance 5^2 = 25, and 25>20 we can
generalize and limit our search till squared root of k. The rest of prime numbers
will have exponent equals to 1.

find_smallest_num() in conjunction with find_all_primes_below() produce the
smallest number that can be divisible from numbers 1 through 'lim_divsor'.
"""

import time
import math
from lib import utilities as utl


def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


def find_smallest_num(lim_divisor):
    primes = utl.find_all_primes_below(20)
    num_primes = len(primes)
    exp_vec = [1]*num_primes
    lim = int(math.sqrt(lim_divisor)+1)
    i = 0
    while primes[i] <= lim:
        exp_vec[i] = math.floor(math.log(lim_divisor)/math.log(primes[i]))
        i += 1
    smallest_num = multiply([primes[i]**exp_vec[i] for i in range(num_primes)])
    return smallest_num


start = time.time()
print(find_smallest_num(20))
print(time.time()-start)
