#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:23:40 2018

@author: jeff
"""

#I created three functions to solve this problem
#First function (list_of_primes) takes an input arugment (in this case 2,000,000) and checks whether the numbers leading up to the input are prime. It does this by calling the second function (isprime) to see if the number is prime, and if so it adds the number to a list of prime numbers. 
#The second function (isprime), checks whether the number of prime by taking the number and dividing it by all the values leading up to the number. Digits that do not divide cleanly into the number are considered prime. 
#the last function (calculate_sum) sums all of the numbers within the list of prime numbers. 

''
def isprime(number):
        if number <= 1:
            return False
        if number == 2:
            return False
        if number % 2 == 0:
            return False
        for i in range(3,int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    

def list_primes(number):
    list_of_primes = []
    for i in range(2,number):
        if isprime(i) == True:
            list_of_primes.append(i)
    calculate_sum(list_of_primes)


    

def calculate_sum(list_of_primes):
    rolling_sum = 0
    for num in list_of_primes:
        rolling_sum += num
    print (rolling_sum)
        
    

list_primes(2000000)

