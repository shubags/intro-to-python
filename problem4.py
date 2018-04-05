"""
Created on Sat Mar 17 12:22:26 2018
@author: patricio

Three functions were defined:

1) is_palindrome: Receives a number and determines if the number is a palindrome.
    
2) multiply: Given a list of numbers, it computes the product of the elements
    
3) find_largest_prime_factor: This function computes the cross product between
    two lists.
"""

def is_palindrome(num):
    if str(num) == ''.join(reversed(str(num))):
        return True
    else:
        return False

def multiply(numbers):  
    total = 1
    for num in numbers:
        total *= num  
    return total 

def get_all_prods(num_list1, num_list2):
    cross_prod_list = list(((x,y) for x in num_list1 for y in num_list2))
    mult_vec = set([multiply(lst) for lst in cross_prod_list])
    return mult_vec

nums = list(range(100,1000))
mult_list = get_all_prods(nums,nums)

palindrome_list = [num for num in mult_list if is_palindrome(num)]
result = max(palindrome_list)
    
print(result)
