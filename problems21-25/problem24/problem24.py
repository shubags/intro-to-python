
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 09:44:15 2018

@author: jeff
"""

numbers = ('0123456789')



def convert_to_list(number):
    listed = []
    [listed.append(x) for x in number]
#    return listed
    r = ''.join(find_permutations(listed)[999999])
    return int(r)
    



def find_permutations(list1):
    
    if len(list1) == 0:
        return []
    
    if len(list1) == 1:
        return [list1]
    
    empty_list = []
    
    for num in range(len(list1)):
#        print (len(list1))
#        print ("num is now:", num)
        
        x = list1[num]
#        print ("x is now:", x)
        
        remainder = list1[:num] + list1[num + 1:]
        
#        print ('remainder:', remainder)
        
        for item in find_permutations(remainder):
            empty_list.append([x] + item)
#            print ('empty_list', empty_list)
        
    
    return empty_list


convert_to_list(numbers)


















