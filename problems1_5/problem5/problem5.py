#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:03:40 2018

@author: jeff
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:27:53 2018

@author: jeff
"""

# =============================================================================
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# =============================================================================


def smallest_positive_evenly_divisible(number):
   
    list_of_numbers = [*range(2,number+1)]
    
    for num in range(2520,999999999,2520):
        if all(num % x == 0 for x in list_of_numbers):
            return num
        else:
            None

smallest_positive_evenly_divisible(20)