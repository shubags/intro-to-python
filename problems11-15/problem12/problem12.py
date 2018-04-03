#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:08:19 2018

@author: jeff
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 09:40:29 2018

@author: jeff
"""



def find_triangle_factors(number):
    
    status = True
    start = 1
    
    while status:
        
        num_factors = 0
        
        triangle_sum = (start * (start + 1))/2
        
        for num in range(1, int(triangle_sum ** 0.5)):
            
            if triangle_sum % num == 0:
                num_factors += 2
                
            if num_factors == number:
                return triangle_sum
                status = False
                break
            
        start += 1
        
    
find_triangle_factors(500)              
      
        
