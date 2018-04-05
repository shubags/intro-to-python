# This module contain useful functions to solve the problems


def sum_if_mult(nums, div_lst):
    if type(div_lst) == list:
        sum_result = sum([i for i in nums if any([i % num == 0 for num in div_lst])])
    else:
        sum_result = sum([i for i in nums if i % div_lst == 0])
    return sum_result


def find_all_primes_below(n):
    prime_list = [True for i in range(n)]
    p = 2
    condition_meet = False
    while condition_meet is False:
        nums_crossed = 0
        if prime_list[p]:
            for i in range(p*2, n, p):
                if prime_list[i] is not False:
                    prime_list[i] = False
                    nums_crossed += 1
        # if for thee previous prime all numbers have been crossed (meaning
        # numbers_crossed variable is equal to 0) then all
        # remaining numbers are prime
        if nums_crossed < 1:
            condition_meet = True
        else:
            p += 1
    list_of_primes = [i for i in range(2,n) if prime_list[i] == True]
    return list_of_primes
