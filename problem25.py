"""
Created on Sun Mar 25 00:52:34 2018

@author: patricio
"""
import time

def compute_fib_term(n):
    fib = []
    fib += [1,1]
    if n > 2:
        for i in range(2,n):
            fib += [fib[i-2] + fib[i-1]]
    return fib[n-1]

start = time.time()

n = 12
num_digits = 2
while(True):
    term = compute_fib_term(n)
    num_digits = len(str(term))
    if num_digits < 1000:
        n += 1
    else:
        break
print(n)


print(time.time() - start)
