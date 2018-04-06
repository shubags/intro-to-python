#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:40:15 2018

@author: jeff
"""


# =============================================================================
# I created multiple mini functions to complete this problem
# =============================================================================


#First list out the days of the week and number of days in each month (depending on year type, regular vs. leap)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_month_regular = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
days_month_leap = ['31', '29', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']


# =============================================================================
# Create function to create list all of the 'first days of the month', using the 'number of years' as the initial input 
# =============================================================================
def first_of_month(years):
    days = 0
    first_day_list = [1]
    
    for i in range(1, years + 1):
        
        for x in range(1, 13):
            
            days += 1
            
            if x == 2 and i % 4 == 0:
                
                leap = int(first_day_list[-1]) + 29
                first_day_list.append(leap)
                
            elif x == 2 and i % 4 != 0:
                
                non_leap = int(first_day_list[-1]) + 28
                first_day_list.append(non_leap)
            
            elif x in (4, 6, 9, 11):
                
                a = int(first_day_list[-1]) + 30
                first_day_list.append(a)
            
            else:
                
                b = int(first_day_list[-1]) + 31
                first_day_list.append(b)
    
    return (first_day_list)





# =============================================================================
# Create function to obtain the total number of days for the input (e.g. 100 years has 35625 days)
# =============================================================================
def days_in_year(years):
    
    total_days_in_year = 0
    
    for x in range(1, years + 1):
     
        if x % 4 != 0:
            total_days_in_year += 365
            
        elif x % 4 == 0:
            total_days_in_year += 366
            
    return total_days_in_year
    



# =============================================================================
# Create function to continuously iterate through the days of the week (Monday --> Sunday)
# If the iteration is on a Sunday and the total_day count is a 'first day of the month', then that sunday
# lands on the first day of the month!
# =============================================================================

def number_of_sundays(years):
    
    number_of_days = days_in_year(years)

    sunday_count = 0
    total_days = 0
    
    while total_days < number_of_days:
        
        for day in days:
            
    #        print (day)
    #        print (total_days)
                    
            if (day == 'Sunday') and (total_days in first_of_month(years)):
                sunday_count += 1       
                
            total_days += 1
            
        
    print (sunday_count)


number_of_sundays(100)
























   
        