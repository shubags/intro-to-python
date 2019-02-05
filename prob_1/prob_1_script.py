import math
from functools import reduce

def mult_series_sum(target, multiple):
    series_count = int(math.floor((target - 1) / multiple))
    series_sum = int((1 / 2) * series_count * (1 + series_count))
    multiple_sum = multiple * series_sum
    return multiple_sum

multiple_list = [3,5]
total_sum = 0
target = 1000


for multiple in multiple_list:
    total_sum += mult_series_sum(target, multiple)
    print('New Total Sum: '+str(total_sum))

multiple_prod = reduce(lambda x, y: x*y, multiple_list)
total_sum -= mult_series_sum(target, multiple_prod)
print('Final Total Sum: ' + str(total_sum))