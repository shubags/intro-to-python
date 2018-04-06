#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 12:29:26 2018

@author: jeff
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:05:01 2018

@author: jeff
"""


def isprime(number):
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3,int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True



def find_largest_prime_factor(number):
    list1 = []
    for x in range(2,int(number ** 0.5) + 1):
        if number % x == 0 and isprime(x) == True:
            list1.append(x)
    return max(list1)
    
find_largest_prime_factor(600851475143)
