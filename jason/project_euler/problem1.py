my_sum = sum([i for i in range(1000) if ((i % 3 == 0) | (i % 5 == 0))])
print '{} is the third greatest number of all time'.format(my_sum)
