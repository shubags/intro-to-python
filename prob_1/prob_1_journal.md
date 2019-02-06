This seems to be a sum of arithmetic series problem. 
Basically, you break down the first given example as follows:

To sum all **_n_** multiples of **_x_**:

1. Take floor value of x (10) divided by n (3). Result: 3

2. Find sum of arithmetic series 1 to 3 using formula:
S(n) = (1/2) * n(a1 + an)
=> S(3) = (1/2) * 3(1 + 3)
=> S(3) = (1/2) * 12
=> S(3) = 6. Result: 6

3. Multiply sum by multiple amount n (3). Result: 18

Repeat this process for 5, and then sum the two results to find the answer.

**NOTE:** This method will double count values that are both multiples of 3 AND 5 (i.e. multiples of 15). 
Thus, will need to add final step of subtracting sum of arithmetic series for multiples of 15 to return final result.  
