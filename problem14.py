"""
Created on Thu Mar 22 11:02:42 2018

@author: patricio
"""

import time

def compute_collatz_starting_at(n):
    collatz_list = [n]
    while(n != 1):
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        collatz_list.append(n)
    return collatz_list

def return_tuple_max_2_elem(tuple_list):
    max_tuple = max(tuple_list, key=lambda x:x[1])
    return max_tuple

start = time.time()

coll_tup_list = []
for i in range(2,1000000):
    coll_list = compute_collatz_starting_at(i)
    new_tup = (i, len(coll_list))
    coll_tup_list.append(new_tup)

max_tuple_coll = return_tuple_max_2_elem(coll_tup_list)

print(max_tuple_coll)

print(time.time()-start)
