"""
=== Question J ===
"""

'''
Q 1 - State what the following Python programs calculate, and explain why:
Q 1a - { 0:"zero", 1:"one", 2:"two" }[1]
A 1a - This would return the string "one", as it is the value associated with
       the key (which was 1). It is important to note that it is not the index,
       and would return the same value no matter the order of the list.

Q 1b - range(1000)[0]
A 1b - It would return zero, as range(1000) is a list of the numbers from 0 to
       999. [0] is the index and the number in the first position in the list
       (index 0) is zero.

Q 1c - for x in range(1,1000): print(list(enumerate(range(x)))[0][0])
A 1c - This would print out 999 copies of the number 0. This is because it
       iterates 999 times, and in each iteration it creates a list of tuples
       with each tuple containing an index and a value. The size of this list is
       equal to the iteration count you are on. However the length of this list is
       irrelevant as we only care about the first element of the first tuple
       which will always be zero (as the index of the first element will always
       be zero), and that index is printed out.

Q 1d - "hello world"[:-2]
A 1d - This returns the string minus the second two characters. This is because
       a string is just a sequence of characters and [:-2] represents the range
       from the very start of the string (part before the colon) up to two
       characters before the end of the string (part after the colon)


Q 2 - Explain the difference in behavior between the following two code snippets:
        x=[""] # Snippet 1
        for i in x: x.append("")
        x=[""] # Snippet 2
        for i in x[:]: x.append("")
A 2 - The first snippet uses the object x on each iteration and loops that many
      time. As each loop increases the size of x, it also increases the amount
      of iterations which are needed. The second one makes a copy of x and
      iterates according to that. That copy is not changed each loop.

Q 3 - Explain the behavior of the following code snippet:
        x=[[]] ; x[0].extend(x)
        while True:
          print(x)
          x = x[0]
A 3 - The first line of the snippet sets x to equal a list containing the empty
      list and then puts x inside of x. This is not a copy however, so x[0]
      contains a reference to itself such that x[0] is x[0][0] is x[0][0][0]
      etc. The snippet on the next lines continues to "dive deeper" into the
      list, by printing out the list and then removing a layer of the list from
      the highest level. Essential falling down an infinitely long hole of a
      python list!


Q 4 - This snippet dosen't work. Explain what the error is and why it arises.
        {[0]:0}[[0]]
A 4 - Python does not support lists as keys in dictionaries. The reason for
      this is that lists work in a way that a list (for example x = [1,2,3],
      and x is used as a key in a dictionary) can be modified with methods such
      as append. If we appended to x, the key in the dictionary will be
      modified which is not reliable. (i.e they are not mutable). This can be
      overcome by using a mutable object such as a tuple instead (or even just
      a number or a string).


Q 5 - Using list comprehensions and lambda, write a program that if given a
      number n, calculates the first n even numbers (starting from 0).
A 5 - '''


# filter in-built
def evenNumbs(n):
    return list(filter(lambda x: x % 2 == 0, range(n * 2)))


# filter manual
def evenNumbs2(n):
    return [i for i in range(n * 2) if (lambda x: x % 2 == 0)(i)]


# map in-built
def evenNumbs3(n):
    return list(map(lambda x: x * 2, range(n)))


# map manual
def evenNumbs4(n):
    return [(lambda x: x * 2)(i) for i in range(n)]


# Tests
print(evenNumbs(10))  # Expect [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(evenNumbs2(10))  # Expect [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(evenNumbs3(10))  # Expect [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(evenNumbs4(10))  # Expect [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

'''
Q 6 - Using list comprehensions and lambda, write a program that if given a
      list of numbers l, will return the sublist of those numbers in l that are
      divisible by 3.
A 6 -'''


# Manual filter
def subListDiv3(l):
    return [i for i in l if (lambda x: x % 3 == 0)(i)]


# In-built filter
def subListDiv3Two(l):
    return list(filter((lambda x: x % 3 == 0), l))


# Tests
print(subListDiv3([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Expect [3, 6, 9]
print(subListDiv3Two([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Expect [3, 6, 9]

'''
Q 7 - The zip function inputs two lists (which you may assume have the same
      length) and outputs the list of pairs of the lists ‘zipped’ together
A 7 - '''


def myZip(l1, l2):
    return [(l1[i], l2[i]) for i in range(len(l1))]


# Test
print(myZip([1, 2, 3], ['one', 'two', 'three']))  # Expect [(1, 'one'), (2, 'two'), (3, 'three')]

'''
Q 8 - Using list comprehensions if possible, write a Python program that
      calculates a list of numbers that are both square and pentagonal
A 8 - '''


def pentSquare(lim):
    pent = [x * (3 * x - 1) // 2 for x in range(lim)]
    squares = [x * x for x in range(lim)]
    return [y for y in squares for x in pent if x == y]


# Test
print(pentSquare(10000))  # Expect [0, 1, 9801, 94109401]

'''
Q 9 - Write programs nest and unnest which translate between nonnegative
      integers and the nesting implemenation. Implement addition and
      multiplication as direct functions on this implementation
A 9 -'''


def nest(n):
    if n == 0:
        return []
    else:
        return [nest(n - 1)]


def unnest(n):
    if not n:
        return 0
    else:
        return 1 + unnest(n[0])


# Sum
def sum_nest(l1, l2):
    if not l1:
        return l2
    else:
        return [sum_nest(l1[0], l2)]


# Multiply
def mult_nest(multiplier, value, total=0):
    if not total:
        return mult_nest(multiplier, value, value)
    elif not multiplier:
        return []
    elif not value:
        return mult_nest(multiplier[0], total, total)
    else:
        return [mult_nest(multiplier, value[0], total)]


# Tests
x = nest(26)
y = nest(10)
print(y)  # Expect [[[[[[[[[[[]]]]]]]]]]]
print(unnest(sum_nest(x, y)))  # Expect 36
print(unnest(mult_nest(x, y)))  # Expect 260
