"""
Created on Tue Mar 20 10:16:53 2018
@author: patricio

Let's use the fact that we can express a Pythagorean triplet in terms of
two numbers m,n using the following relationships.

       a = m^2 - n^2
       b = 2 * m * n
       c  = m^2 + n^2
because,
       a^2 = m^4 + n^4 – 2*m^2*n^2
       b^2 = 4*m^2*n^2
       c^2 = m^4 + n^4 + 2*m^2*n^2

By looping over m, n we can generate pythagorean triplets instead of trying to
loop over the three numbers (a, b, c)

"""

def build_pythagorean_triplets(limit):
    m = 2
    c = 0
    pythagorean_list = []
    #limiting c will also in consequence limit a and b
    while(c < limit):
        for n in range(1,m):
            a = m**2 - n**2;
            b = 2*m*n;
            c = m**2 + n**2;
            if c > limit:
                break
            new_pyth = [a,b,c]
            pythagorean_list.append(new_pyth)
        m += 1
    return pythagorean_list

"""
We want to compute all pythagorean triplets which not exceed limit = 1000
for c and then we're going to find which of those triplets satisfy
a + b + c = 1000
"""

pyth_list = build_pythagorean_triplets(1000)

sum_of_pyth_list = [lst for lst in pyth_list if sum(lst) == 1000]

pyth_result = sum_of_pyth_list[0]

print(pyth_result)
print(pyth_result[0]*pyth_result[1]*pyth_result[2])

