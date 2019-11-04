"""
Created on Mon Mar 19 03:24:46 2018
@author: patricio

In mathematics, the sieve of Eratosthenes is a simple, ancient algorithm for 
finding all prime numbers up to any given limit.

To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

1) Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    
2) Initially, let p equal 2, the smallest prime number.
    
3) Enumerate the multiples of p by counting to n from 2p in increments of p, 
    and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself 
    should not be marked).
    
4) Find the first number greater than p in the list that is not marked. 
    If there was no such number, stop. Otherwise, let p now equal this new number 
   (which is the next prime), and repeat from step 3.

5) When the algorithm terminates, the numbers remaining not marked in the list
 are all the primes below n.

"""
import time

def find_all_primes_below(n):
    prime_list = [True for i in range(n)]
    p = 2
    condition_meet = False
    while(condition_meet == False):
        if prime_list[p] == True:
            nums_crossed = 0
            for i in range(p*2, n, p):
                if prime_list[i] != False:
                    prime_list[i] = False
                    nums_crossed += 1      
        #if for thee previous prime all numbers have been crossed (meaning
        #numbers_crossed variable is equal to 0) then all
        #remaining numbers are prime
        if nums_crossed < 1:
            condition_meet = True
        else:
            p += 1
    list_of_primes = [i for i in range(2,n) if prime_list[i] == True]
    return list_of_primes
                
start = time.time()

    
prime_list = find_all_primes_below(2000000)
    
print(sum(prime_list))
#142913828922
print(time.time()-start)

