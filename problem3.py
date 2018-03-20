"""
Created on Fri Mar 16 23:27:24 2018
@author: patricio

For Solving Problem 3 in Project Euler.

Three functions were defined:

1) is_prime: Receives a number and determines if the number is prime.
    
2) find_next_prime_num_after: Returns the next prime number that follows
    the imputed number
    
3) find_largest_prime_factor: This function calculates all prime factors
    by starting at the smallest prime and working upwards. Then it returns
    the maximum of the list.
"""

def is_prime(number):
    default = True
    if number in [0,1]:
        default = False
    elif number == 2:
        default = True
    else:
        for i in range(2,number//2+1):
            if number % i == 0:
                default = False
                break
    return default

def find_next_prime_num_after(num):
    condition_meet = False
    if num % 2 == 0:
        k = num//2 #Since we're only checking numbers of the form 2k+1
    else:
        k = num//2 + 1
    num = 2*k + 1 
    while(condition_meet == False):
        if(is_prime(num)):
            condition_meet = True
        else:
            k+=1
            num = 2*k+1 #This reduces numbers of loops by eliminating all even numbers
    return num


def find_largest_prime_factor(num):
    prime_fact_list = []
    aux = 2
    while(aux <= num):
        if (num%aux==0):
            prime_fact_list.append(aux)
            num = num / aux
        else:
            aux = find_next_prime_num_after(aux)
    return max(prime_fact_list)

print(find_largest_prime_factor(600851475143))
