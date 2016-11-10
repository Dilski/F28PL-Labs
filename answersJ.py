# === Question J ===

# 1 - State what the following Python programs calculate, and explain why:
#       Q - { 0:"zero", 1:"one", 2:"two" }[1]
#       A - This would return the string "one", as it is the value associated with the key (which wa 1).
#           It is important to note that it is not the index, and would return the same value no matter
#           The order of the list.
#       Q - range(1000)[0]
#       A - It would return zero, as range(1000) is a list of the numbers from 0 to 999. [0] is the index
#           and the number in the first position in the list (index 0) is zero.
#       Q - for x in range(1,1000): print(list(enumerate(range(x)))[0][0])
#       A - This would print out 999 copies of the number 0. This is because it iterates 999 times, and
#           in each iteration it creates a list of tupples with each tupple containing an index and a value.
#           The size of this list is equal to the iteration count you are on. However the length of this list is irrelevent
#           as we only care about the first element of the first tupple which will always be zero (as the index of the
#           first element will always be zero), and that index is printed out.
#       Q - "hello world"[:-2]
#       A - This returns the string minus the second two characters. This is because a string is just a sequence of characters
#           and [:-2] represents the range from the very start of the string (part before the colon) up to two characters before
#           the end of the string (part after the colon)
#
# Explain the difference in behaviour between the following two code snippets:
#
#     x=[""] # Snippet 1
#       for i in x: x.append("")
#     x=[""] # Snippet 2
#       for i in x[:]: x.append("")
#
#       A - The first snippet uses the object x on each iteration and loops that many time. As each loop increaces the size of x,
#           it also increases the amount of iterations which are needed. The second one makes a copy of x and iterates according to
#           that. That copy is not changed each loop.
#
#     Explain the behaviour of the following code snippet:
#     x=[[]] ; x[0].extend(x)
#	while True:
#	   print(x)
#	   x = x[0]
#
#
#      Thie first line of the snippet sets x to equal a list containing the empty
#      list and then puts x inside of x. This is not a copy however, so x[0] contains
#      a reference to itself such that x[0] is x[0][0] is x[0][0][0] etc.
#      The snippet on the next lines continues to "dive deeper" into the list, by 
#      printing out the list and then removing a layer of the list from the highest
#      level. Essential falling down an infinately long hole of a python list! 
#
#
#      This snippet dosen't work. Explain what the error is and why it arises.  
#        {[0]:0}[[0]]
#      Python does
#      not support lists as keys in dictionaries. The reason for this is that lists
#      work in a way that a list (for example x = [1,2,3], and x is used as a key in
#      a dictionary) can be modified with methods such as append. If we appended to 
#      x, the key in the dictionary will be modified which is not reliable. (i.e 
#      they are not mutable). This can be overcome by using a mutable object such as #      a tupple instead (or evene just a number or a string).
#
#	Using list comprehensions and lambda, write a program that if given a 
#       number n, calculates the first n even numbers (starting from 0).
def evenNumbs(n):
	return list(filter(lambda x: x % 2 == 0, range(n*2)))

# alternatively

def evenNumbs2(n):
	return list(map(lambda x: x * 2, range(n)))

# also

# filter
def evenNumbs3(n):
	return [i for i in range(n*2) if (lambda x: x % 2 == 0)(i)]

# map
def evenNumbs4(n):
	return [(lambda x: x*2)(i) for i in range(n)]

# the last two are just manual versions of the first two evenNumbs

print(evenNumbs(10))
print(evenNumbs2(10))
print(evenNumbs3(10))
print(evenNumbs4(10))

# 5 - Using list comprehensions and lambda, write a program that if given a list 
#     of numbers l, will return the sublist of those numbers in l that are 
#     divisible by 3.

def subListDiv3(l):
	return [i for i in l if (lambda x: x % 3 == 0)(i)]

def subListDiv3Two(l):
	return list(filter((lambda x: x % 3 == 0), l))

print(subListDiv3([1,2,3,4,5,6,7,8,9]))
print(subListDiv3Two([1,2,3,4,5,6,7,8,9]))

# 6 - The zip function inputs two lists (which you may assume have the same 
#     length) and outputs the list of pairs of the lists 'zipped' together.

def myZip(l1,l2):
	return [(l1[i],l2[i]) for i in range(len(l1))]


print(myZip([1, 2, 3], ['one', 'two', 'three']))

def pentSquare(lim):	
	
	pent = [x*(3*x-1)//2 for x in range(lim)]

	squares = [x*x for x in range(lim)]

	return [y for y in squares for x in pent if x == y] 


print(pentSquare(10000))



def nest(n):
	if n==0:
		return []
	else:
		return [nest(n-1)]


