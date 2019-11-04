"""
Created on Sun Mar 18 19:05:55 2018
@author: patricio

1) is_prime: Receives a number and determines if the number is prime.
    
2) find_next_prime_num_after: Returns the next prime number that follows
    the imputed number
    
"""
import time

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

start = time.time()

prime_num = 2
prime_pos = 1

while(prime_pos < 10001):
    prime_num = find_next_prime_num_after(prime_num)
    prime_pos += 1
    
print(prime_num)

print(time.time()-start)

