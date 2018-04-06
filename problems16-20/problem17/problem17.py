#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:41:51 2018

@author: jeff
"""

numDict = { 
0:"zero",
1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten",
11:"eleven",
12:"twelve",
13:"thirteen",
14:"fourteen",
15:"fifteen",
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"forty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety",
100:"hundred"
}


def find_sum_length(number):
    
    letter_sum = 0
    
    for num in range(1, number +1):
        if num <= 20: #for single digits and tens
            letter_sum += len(numDict[num])
                     
        elif 20 < num < 100: #for numbers above 20
            foo, bar = int(str(num)[0]), int(str(num)[1])
            if int(bar) == 0:
                letter_sum += len(numDict[foo * 10])
            else:
                letter_sum += (len(numDict[foo * 10]) + len(numDict[bar]))         
                
        elif 100 <= num < 1000: #for hundreds
            if num % 100 == 0:
                letter_sum += (len(numDict[int(num / 100)]) + len(numDict[100]))
                
            else:
                hundreds, foo, bar = int(str(num)[0]), int(str(num)[1]), int(str(num)[2])
                
                if int(str(num)[1:3]) < 10:
                    letter_sum += (len(numDict[hundreds]) + len(numDict[100]) + len('and') + len(numDict[int(str(num)[2])]))
   
                elif 10 <= int(str(num)[1:3]) < 20: #e.g. hundred and eleven
                    letter_sum += (len(numDict[hundreds]) + len(numDict[100]) + len('and') + len(numDict[int(str(num)[1:3])]))  
                    
                else: #e.g. hundred and twenty four
                    if int(bar) == 0:
                        letter_sum += (len(numDict[hundreds]) + len(numDict[100]) + len('and') + len(numDict[(foo * 10)]))
                    else:
                        letter_sum += (len(numDict[hundreds]) + len(numDict[100]) + len('and') + len(numDict[(foo * 10)]) + len(numDict[bar]))   
        
        elif num == 1000:
            letter_sum += len('onethousand')
        
    return letter_sum                              
                    
find_sum_length(1000)
                    
                    
                    
                    
                    
                    
                    
                 
        