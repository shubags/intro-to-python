"""
Created on Fri Mar 23 10:18:26 2018

@author: patricio
"""

def is_leap_year(year):
    if str(year)[2:4] == '00':
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


month_day_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,
                  10:31, 11:30, 12:31}

all_sunday_list = []
sunday_month_lst = []
first_sunday = 6
next_sunday = first_sunday + 7
sunday_month_lst += [first_sunday, next_sunday]
for year in range(1901, 2001):
    for i in range(1,13):
        if is_leap_year(year) and i == 2:
            num_days = 29
        else:
            num_days = month_day_dict[i]
        while(next_sunday+7 <= num_days):
            next_sunday += 7
            sunday_month_lst.append(next_sunday)
        all_sunday_list.append(sunday_month_lst)
        sunday_month_lst = []
        first_sunday = 0 + 7 - (num_days - next_sunday)
        next_sunday = first_sunday + 7
        sunday_month_lst += [first_sunday, next_sunday]
        
sunday_count = 0
for lst in all_sunday_list:
    for day in lst:
        if day == 1:
            sunday_count += 1
            
print(sunday_count)
