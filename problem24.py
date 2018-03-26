"""
Created on Sun Mar 25 00:42:33 2018
@author: patricio

get_permutations uses a backtracking alorithm to get the permutations of the
elements of a list.
See top answer in
#https://cs.stackexchange.com/questions/80223/using-backtracking-to-find-all-possible-permutations-in-a-string
"""
import time

def get_permutations(lst, st_idx, num_elems, sv_lst = None):
    if sv_lst is None:
        sv_lst = []
    if num_elems == st_idx:
        new_list = lst.copy()
        sv_lst.append(new_list)
    else:
        for i in range(st_idx, num_elems):
            lst[st_idx], lst[i] = lst[i], lst[st_idx]
            get_permutations(lst, st_idx + 1, num_elems, sv_lst)
            lst[st_idx], lst[i] = lst[i], lst[st_idx]
    return sv_lst

num_lst = [str(i) for i in range(10)]

start = time.time()

perm_lst = get_permutations(num_lst, 0, 10)
str_perm_lst = [''.join(digits) for digits in perm_lst]
str_perm_lst.sort()
print(str_perm_lst[999999])


print(time.time() - start)
