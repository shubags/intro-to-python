# This module contain useful functions to solve the problems


def sum_if_mult(nums, div_lst):
    if type(div_lst) == list:
        sum_result = sum([i for i in nums if any([i % num == 0 for num in div_lst])])
    else:
        sum_result = sum([i for i in nums if i % div_lst == 0])
    return sum_result

