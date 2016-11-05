from functools import reduce

# ===Question H === #

print("-- Part 1 --")
'''
Q - Using iteration (a for-next or a while loop or similar), write a program
    mult1 that if given a list of integers or reals will return their product
    (the result of multiplying all the numbers together).
'''


def mult1(num_list):
    """
    :param num_list: List of reals or integers.
    :return: product of the numbers in the list.
    """
    result = 1
    while num_list:
        result *= num_list.pop(0)
    return result


print(mult1([]))  # expect 1
print(mult1([1, 2, 3, 10]))  # expect 60


print("-- Part 2 --")
"""
Q - Using recursion, write a program mult2 that if given a list of integers or
    reals will return their product
"""


def mult2(num_list):
    """
    :param num_list: List of reals or integers.
    :return: product of numbers in the list.
    """
    if num_list:
        return num_list.pop(0) * mult2(num_list)
    else:
        return 1


print(mult2([]))  # expect 1
print(mult2([1, 2, 3, 10]))  # expect 60


print("-- Part 3 --")
'''
Q - Write a one-line piece of code that breaks mult2
A - This happens because python has a default maximum recursion depth of 999
'''
try:
    print(mult2(list(range(1, 1000))))
except Exception:
    print("Caught Exception")


print("-- Part 4 --")
"""

"""


def mult3(num_list):
    """
    :param num_list: List of reals or integers.
    :return: product of numbers in the list.
    """
    if num_list:
        return reduce(lambda x, y: x * y, num_list)
    else:
        return 1


print(mult3([1, 2, 3, 10]))  # expect 60
print(mult3([]))  # expect 1


print("-- Part 5 --")
'''
Q - What do mult1, mult2, and mult3 return if applied to [1.0,2,3.0,10]? What would
    corresponding programs do if they were written in ML and applied to such an
    input? What does this tell us about ML vs Python typing?
'''

print(mult1([1.0, 2, 3.0, 10]))
print(mult2([1.0, 2, 3.0, 10]))
print(mult3([1.0, 2, 3.0, 10]))
'''
A - All three of the functions return 60.0 when given [1.0, 2, 3.0, 10] In ML,
    these three functions would not run with this input, as it is not a valid input.
    ML does not allow multiple types in a list. If this is somehow bypassed, ML
    would not be able to multiply a real by an int. This shows that python has
    lazier types, which are not as strict.
'''


print("-- Part 6 --")
'''
Q - Order mult1, mult2, and mult3 from slowest to fastest and explain your order.
    There is no single “right” answer here, and this is a theoretical question,
    not an empirical one; you are welcome to measure performance but what
    interests me is your understanding.

A - I beleive that mult1 would be the fastest, ad it is simply, adding up the
    numbers as it goes along the array, whereas the other two methods have to move
    to the end of the array and back again, returning numbers on it's return.

    I am convinced that mult2 and mult3 would take the same amount of time as they
    are basically the same. However as mult3 runs a function that adds as it goes
    along, and is such quicker.

    Therefore: (fastest) mult1 -> mult3 -> mult2 (slowest)
'''


print("-- Part 7 --")
'''
Q - Write a program multpoly that outputs the product of a list of numbers,
    and the concatenation (i.e. chaining) of a list of strings or lists.
'''


def multpoly(poly_list):
    """
    :param poly_list: List of numbers, strings or lists
    :return: product of numbers, or concatenation of other types.
    """

    def concat(concat_list):
        result = concat_list.pop(0)
        while concat_list:
            result += concat_list.pop(0)
        return result

    list_type = type(poly_list[0])

    if (list_type is int) or (list_type is float):
        return mult1(poly_list)
    elif (list_type is str) or (list_type is list):
        return concat(poly_list)


print(multpoly([1, 2, 3, 10]))  # 60
print(multpoly(["1", "2", "3", "10"]))  # "12310"
print(multpoly([[1], [2, 3], [10]]))  # [1,2,3,10]


print("-- Part 7 --")
'''
Q - write a recursive program flatten that inputs an arbitrarily nested
    list structure and outputs a “flattened” list consisting of the list of
    all the data in the list, but with any nested list structure removed.
'''


def flatten(input_list):
    """
    :param input_list: List to flatten.
    :return: Flattened list.
    """
    if not input_list:
        return input_list
    else:
        pop = input_list.pop(0)
        if type(pop) is list:
            return flatten(pop) + flatten(input_list)
        else:
            return [pop] + flatten(input_list)


print(flatten([]))  # []
print(flatten([["hi"], 5]))  # ["hi",5]
print(flatten([[[], [["hello"], [" "]], [1], [[["world"]], []]], "!"]))  # ["hello"," ",1,"world!"]
