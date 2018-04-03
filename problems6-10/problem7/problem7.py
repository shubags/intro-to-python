#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:05:01 2018

@author: jeff
"""

#decided to create two functions to solve this problem

#first function takes a number input as an argument and creates a list of prime numbers. In order for this function to know whether the value is prime, it calls function "isprime"
#second function (isprime) takes a number and returns whether the number is prime or not (returns boolean)




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
    
    

def find_x_prime_number(number):
    
    increment = 2
    list_of_primes = []
    
    while len(list_of_primes) < number:
        if isprime(increment) == True:
            list_of_primes.append(increment)
        increment += 1
    
    
    print (list_of_primes)

find_x_prime_number(10001)


