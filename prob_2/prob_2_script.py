
def is_even(test_number):
    if test_number % 2 == 0:
        return True
    else:
        return False


limit = 4000000
fib_num_1 = 0
fib_num_2 = 1
fib_sum = 0

while True:
    fib_num_3 = fib_num_1 + fib_num_2
    if fib_num_3 >= limit:
        break
    fib_num_1 = fib_num_2
    fib_num_2 = fib_num_3
    print('New Fib Number: ' + str(fib_num_2))
    if is_even(fib_num_2):
        fib_sum += fib_num_2
        print('New Fib Running Total: ' + str(fib_sum))

print('Final Fib Sum: '+str(fib_sum))
