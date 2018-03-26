"""
Created on Fri Mar 23 15:00:41 2018

@author: patricio
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
    return fact

def sum_digits_num(num):
    suma = 0
    num_str = str(num)
    for i in num_str:
        suma += int(i)
    return suma


print(sum_digits_num(factorial(100)))
