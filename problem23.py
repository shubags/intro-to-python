"""
Created on Sun Mar 25 01:19:48 2018
@author: patricio

get_proper_divisors: computes the divisors of n that are minor to n.

is_abundant_num: evaluates if a number is abundant (i.e the sum of it's 
    divisors is greater than itself.)
    
get_all_sums_lst: returns a list with the sums of each pair of elements that 
    can be drawn in a list. (Returns them without repetition) 

"""

import math
import time

def get_proper_divisors(n):
    all_divisors = [1]
    for i in range(2,int(math.sqrt(n)+1)):
        if (n % i == 0):
            if i == n // i:
                all_divisors += [i]
            else:
                all_divisors += [i, n//i]
    return all_divisors

def is_abundant_num(n):
    flag = True
    if sum(get_proper_divisors(n)) <= n:
        flag = False
    return flag

def get_all_sums_lst(lst):
    cross_prod_list = list(((x,y) for x in lst for y in lst))
    sum_vec = set([sum(lst) for lst in cross_prod_list])
    return sum_vec

start = time.time()

ab_lst = []
for i in range(12 ,28123-12):
    if is_abundant_num(i):
        ab_lst.append(i)

all_sums = get_all_sums_lst(ab_lst)

nlist = set(range(1,28123+1)) - all_sums

print(sum(nlist))

print(time.time() - start)
#4179871