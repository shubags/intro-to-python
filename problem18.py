"""
Created on Fri Mar 23 00:42:07 2018
@author: patricio

Function "num_triangle_to_mat" recieves a triangle made of rows of digits and
separated by \n and transform it into a list of lists.

Several paths can lead you to each one of the numbers in the 
base of the pyramid (except for first and last element from left to right),
however, there's just one path that maximizes the summation of the digits for
each of the numbers previously mentioned.
The function "maxPath_TriangMat" find the summation of the paths mentioned above
and return maximum value.
"""
import time

def num_triangle_to_mat(triangle):
    triangle = triangle.split("\n")
    triangle_lol = []
    for elem in triangle:
        triangle_lol.append([int(num) for num in elem.split(' ')])
    mat_lst = [] 
    for lst in triangle_lol:
        new_list = lst + [0]*(len(triangle_lol[len(triangle_lol)-1])-len(lst))
        mat_lst.append(new_list)
    return mat_lst


def maxCost_TriangMat(cost, m):
    cost_mat = [[0 for x in range(m)] for x in range(m)]
    cost_mat[0][0] = cost[0][0]
    #Compute the accumulated sum for the first column (this computes sum of
    #the route to the first number from left to right in the pyramid)
    for i in range(1, m):
        cost_mat[i][0] = cost_mat[i-1][0] + cost[i][0]
    #We compute the sum of the rest of the paths by selecting to move in
    #any direction based on which is the greatest number
    for i in range(1, m):
        for j in range(1,i+1):
            #We can only make moves by moving down or in diagonal
            cost_mat[i][j] = max(cost_mat[i-1][j-1], cost_mat[i-1][j]) + cost[i][j]
    return max(cost_mat[m-1])
            

triangle = '75\
\n95 64\
\n17 47 82\
\n18 35 87 10\
\n20 04 82 47 65\
\n19 01 23 75 03 34\
\n88 02 77 73 07 63 67\
\n99 65 04 28 06 16 70 92\
\n41 41 26 56 83 40 80 70 33\
\n41 48 72 33 47 32 37 16 94 29\
\n53 71 44 65 25 43 91 52 97 51 14\
\n70 11 33 28 77 73 17 78 39 68 17 57\
\n91 71 52 38 17 14 91 43 58 50 27 29 48\
\n63 66 04 68 89 53 67 30 73 16 69 87 40 31\
\n04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

mat_cost = num_triangle_to_mat(triangle)

start = time.time()

print(maxCost_TriangMat(mat_cost, len(mat_cost[0])))

print(time.time() - start)
