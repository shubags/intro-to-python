"""
Created on Wed Mar 21 16:23:32 2018

@author: patricio
"""
import math
import time

def get_all_divisors(n):
    all_divisors = []
    for i in range(1,int(math.ceil(math.sqrt(n) + 1))):
        if (n % i == 0):
            if i == n // i:
                all_divisors += [i]
            else:
                all_divisors += [i, n//i]
    return all_divisors
        
    
def sum_first_n_numbers(num_nums):
    total_sum = 0
    for i in range(1,num_nums+1):
        total_sum += i
    return total_sum

start = time.time()

divisors = 1
fact_num = 8
while(divisors < 500):
    num = sum_first_n_numbers(fact_num)
    divisors = len(get_all_divisors(num))
    fact_num += 1
print(num)

print(time.time()-start)
