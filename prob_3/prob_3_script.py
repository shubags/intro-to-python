import math
prime_num_list = [2]


def is_even(test_number):
    if test_number % 2 == 0:
        return True
    else:
        return False


def is_factor(dividend, divisor):
    if dividend % divisor == 0:
        return True
    else:
        return False


def is_prime(test_number):
    if test_number in [0, 1] or is_even(test_number):
        return False
    else:
        for prime in prime_num_list:
            if test_number % prime == 0:
                return False
    prime_num_list.append(test_number)
    return True


def prime_factorization(test_number):
    prime_factors = []
    limit = int(math.sqrt(test_number))
    if is_even(test_number):
        prime_factors.append(2)
    for i in range(1, limit, 2):
        if is_factor(test_number, i):
            if is_prime(i):
                prime_factors.append(i)
    print('Prime factors: ' + str(prime_factors))
    return prime_factors


target_num = 600851475143
prime_factor_list = prime_factorization(target_num)
print('The largest prime factor of ' + str(target_num) + ' is ' + str(prime_factor_list[-1]) + '.')
