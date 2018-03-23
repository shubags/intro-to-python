"""
Created on Thu Mar 22 13:09:36 2018
@author: patricio

Commented code was a first approach in which the function permute_list
would compute all possible permutations of elements in a list and then with
get_lattice_paths_on_grid_size we were going to pick paths without repetition.
However this solution proved to be inefficient due the complexity behind the
permutation algorithm, best guess is complexity was O(n*n!).

So a more analytic approach was used, this solution is based on the 
multinomial formula and the fact that for any grid of size m*n we need exactly
m steps to the right and n steps down in the grid in order to move from position
(1,1) to position (m,n)

"""

#Discarded solution
"""
def permute_list(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    perm_list = []
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permute_list(remLst):
           perm_list.append([m] + p)
    return perm_list
 

def get_lattice_paths_on_grid_size(m, n):
    direc_1 = ['Right']*m + ['Down']*n
    direc_list = set(tuple(i) for i in permute_list(direc_1))
    return direc_list


print(len(get_lattice_paths_on_grid_size(20,20)))
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
    return fact

def get_num_lattice_paths_grid_size(m, n):
    num_paths = factorial(m+n)//(factorial(m)*factorial(n))
    return num_paths

print(get_num_lattice_paths_grid_size(20, 20))

