# ===Question I=== #

print("-- Part 1 --")
'''
Q - Write a program factors that inputs a number n, which you may assume is
    greater than 2, and outputs the list of its prime factors (prime numbers
    are 2, 3, 5, 7, 11, 13, 17, and so on). You may assume basic arithmetic
    operations, including modulus n % k and divisibility.
'''


def factors(n):
    """
    :param n: Number to find prime factors of.
    :return: List of prime factors.
    """

    def is_prime(m):
        prime = True
        for i in range(2, m-1):
            if m % i == 0:
                prime = False
                break
        return prime

    if is_prime(n):
        return [n]
    else:
        factor_list = [x for x in range(2, n+1) if (n % x == 0) and is_prime(x)]
        return factor_list

print(factors(123))  # expect [3, 41]
