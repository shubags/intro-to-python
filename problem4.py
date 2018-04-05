"""
Created on Sat Mar 17 12:22:26 2018
@author: patricio

This method looks for the largest palindrome by starting with
the multiplications of the highest numbers, i.e it counts downwards
starting from 999.
"""


def is_palindrome(num):
    return str(num) == ''.join(reversed(str(num)))


largestPal = 0
a = 999
while a >= 100:
    b = 999
    while b >= a:
        if a*b <= largestPal:
            break
        if is_palindrome(a*b):
            largestPal = a*b
        b -= 1
    a -= 1
print(largestPal)
