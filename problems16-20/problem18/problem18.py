
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 17:10:45 2018

@author: jeff
"""

triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

def break_triangle(): #break the triangle into list of list

    x = triangle.split("\n")
    
    t_list = []
    
    for sublist in x:
        t_list.append([int(i) for i in sublist.split(' ')])
    
    return max_path_sum(t_list)


def max_path_sum(t_list):

    r_index = -2 #this index is used to iterate through each row
    index_start = -1 #this index is used to index and reference the individual items within each row
    
    while r_index > -(len(t_list) + 1):
            
        temp_list = [] #create a temporary list, this will be used later to replace the bottom rows of the triangle
        index_end = 0 #this is to index and reference the second object 
        
        for item in t_list[r_index]: #for each item within the second-to-last row in the triangle, take the max of the values to the bottom (bottom-left, bottom-right)
            
            digit1 = t_list[index_start][index_end]
            digit2 = t_list[index_start][index_end + 1]
            
            num = item + max(digit1, digit2)
            temp_list.append(num) #add the max value to the temporary list
            
            index_end += 1 #increase the index to move to the next set of values
            
        del t_list[-2:] #delete the bottom two rows of the triangle, since we combined them into a single row during the 'find max value' portion
        t_list.append(temp_list) #add the temporary list as the new bottom row of the triangle
    
    return t_list[0][0]
    
break_triangle()  

