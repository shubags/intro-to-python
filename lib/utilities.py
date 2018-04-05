# This module contain useful functions to solve the problems


def sum_if_mult(nums, div_nums):
    div_lst = list(div_nums)
    sum_result = sum([i for i in range(nums) if any([i % num == 0 for num in div_lst])])
    return sum_result

