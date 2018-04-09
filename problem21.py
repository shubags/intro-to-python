"""
Created on Fri Mar 23 15:21:09 2018
@author: patricio

d(n) computes the sum of proper divisors of n (numbers less than n which 
     divide evenly into n)

get_all_divisors(n): returns all divisors of a number 'n', including 1 and n.
"""
import math
import time

def get_all_divisors(n):
    all_divisors = []
    for i in range(1,int(math.sqrt(n)+1)):
        if (n % i == 0):
            if i == n // i:
                all_divisors += [i]
            else:
                all_divisors += [i, n//i]
    return all_divisors

def d(n):
    divisors = get_all_divisors(n)
    divisors.remove(n)
    suma = sum(divisors)
    return suma

start = time.time()

amiccable_list = []
set_nums = set(range(2,10000))
while len(set_nums) > 1:
    i = set_nums.pop()
    if i == d(d(i)) and i != d(i): #are i and d(i) an ammicable pair?
        amiccable_list += [i, d(i)]
        set_nums = set_nums - {d(i)}

print(sum(amiccable_list))

print(time.time() - start)

