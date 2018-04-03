#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:22:38 2018

@author: jeff
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 13:31:07 2018

@author: jeff
"""


def lettuce_paths(user_input):
    
    count_paths1 = 1
    count_paths2 = 1
    
    for num in range(1, (user_input*2) +1):
        count_paths1 *= num
    
    for item in range(1, user_input +1):
        count_paths2 *= item
        
    return count_paths1 / (count_paths2 ** 2)

lettuce_paths(20)