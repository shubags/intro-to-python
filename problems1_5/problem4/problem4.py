#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:45:33 2018

@author: jeff
"""
# =============================================================================
# 
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
# =============================================================================

def largest_palindrome(number_of_digits = "3"):
    
    if number_of_digits == "3":
        palindrome = []
        for number1 in range(100,1000):
            for number2 in range(100,1000):
                product = number1 * number2
                if str(product) == str(product)[::-1]:
                    palindrome.append(product)
                
    print (max(palindrome))

largest_palindrome("3")
    

    