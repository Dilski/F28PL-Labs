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
        for i in range(2, m - 1):
            if m % i == 0:
                prime = False
                break
        return prime

    if is_prime(n):
        return [n]
    else:
        factor_list = [x for x in range(2, n + 1) if (n % x == 0) and is_prime(x)]
        return factor_list


print(factors(123))  # expect [3, 41]
print(factors(0))  # expect [3, 41]

print("-- Part 2 --")
'''
Q - Write a program largest that inputs a nonempty list of numbers and
    outputs its greatest element. You do not need to worry about
    error-handling, e.g. if the input is the empty list.
'''


def largest(num_list):
    """
    :param num_list: List to find largest number in.
    :return: Largest number in num_list.
    """
    largest_number = num_list.pop(0)
    while num_list:
        n = num_list.pop()
        if n > largest_number:
            largest_number = n
    return largest_number


print(largest([1, 2, 3, 4, 2]))  # Expect 4

print("-- Part 3 --")
'''
Q - Write a program largest_factor that inputs a number n and
    outputs its largest prime factor.
'''


def largest_factor(n):
    return largest(factors(n))


print(largest_factor(123))  # expect 41

print("-- Part 4 --")
'''
Q - Write a program firstbigfib that inputs a number
    n and outputs the index of the first Fibonacci
    number to contain n digits.
'''


def firstbigfib(n):
    a = 0
    b = 1
    goal = 10 ** (n - 1)
    while True:
        a, b = b, a + b
        if b >= goal:
            return b


print(firstbigfib(4))  # expect 1597

print("-- Part 5 --")
'''
Q - Write a program firstbigf that inputs a number n and
    a function f mapping numbers to numbers, and outputs
    the least strictly positive number i (so i is in [1,2,3,...])
    such that f(i) contains n digits. So for example if f=lambda
    x:10**x then firstbigf f 10 should calculate 9 (because
    10**9, which is equal to 1000000000, has ten digits).
'''


def firstbigf(f, n):
    count = 1
    goal = 10 ** (n - 1)
    while True:
        result = f(count)
        count += 1
        if result >= goal:
            return count


print(firstbigf(lambda z: 10 ** z, 9))  # expect 9

print("-- Part 6 --")
'''
Q - Suggest, in very general terms, how we might optimise
    firstbigf to run on a multicore architecture, with a
    roughly m-fold speedup where m is the number of cores.
A - You could assign threads with a step amount equalling
    the amount of threads being used, and each thread starting
    at it's thread. I.e:

    +--------+------+----------------+------------------+
    | Thread | Step | Start Position | Sequence         |
    +--------+------+----------------+------------------+
    | 1      | 4    | 1              | 1, 5, 9, 13 ...  |
    | 2      | 4    | 2              | 2, 6, 10, 14 ... |
    | 3      | 4    | 3              | 3, 7, 11, 15 ... |
    | 4      | 4    | 4              | 4, 8, 12, 16 ... |
    +--------+------+----------------+------------------+

    Each thread stops once the conditions are met (i.e. when the
    amount of digits exceeds the argument), and all threads
    compare results to find the lowest, and that result is the
    one that is returned.
'''

print("-- Part 7 --")
'''
Q - Using Python generators, write a Python generator function
    triples() to generate all Pythagorean triples
'''
# https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples

def triples():
    m = 2
    while True:
        yield (((m*m) - 1), (2 * m), ((m*m) + 1))
        m += 1

x = triples()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
