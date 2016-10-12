# Programming-Languages-SML

## Question A (Basic SML).

Write SML functions to:

1- Multiply real x by integer y to give a real.
~~~~
- realIntMult 3.3 3;
> 9.9 : real
~~~~

2- Check if string s1 has more letters than string s2.
~~~~
- moreLetters "big" "small";
> false : bool
~~~~

3- Check if character c represents a digit. Do not answer this by writing just Char.isDigit. Also, do not hard-code ASCII numbers such as ‘37’ or ‘42’. This is bad practice, since most readers do not know ASCII encoding off by heart so it is unclear to the reader what represent. 
~~~~
- isDigit #"7";
> true : bool
~~~~

4- If character c represents a digit then return its integer equivalent; otherwise return ~1. Again, your answer should not hard-code ASCII numbers.
~~~~
- digitValue #"a";
> ~1 : int
- digitValue #"7";
> 7 : int
~~~~

5- Convert a real r into a tuple of its value and integer equivalent.
~~~~
- conv 99.99;
> (99.99,99) : real * int
~~~~

6- Implement the NAND function from the truth-table below. Your implementation should not use the ML primitives not, andalso, or orelse. We are looking for you to write a program that is almost identical to the specification of the problem.

| X     | Y     | X NAND Y |
|-------|-------|----------|
| FALSE | FALSE | TRUE     |
| FALSE | TRUE  | TRUE     |
| TRUE  | FALSE | TRUE     |
| TRUE  | TRUE  | FALSE    |

~~~~
- NAND false true;
> true : bool
~~~~

## Question B (Recursion, chaining functions).

1- Find the integer logarithm to the base 2 of an integer n by repeatedly dividing by 2 and counting:
~~~~
log2 1 = 0
log2 n = 1+log2 (n div 2)
- log2 8;
> 3 : int
~~~~

2- Find the square root of an integer x by repeatedly decrementing an initial guess s:
~~~~
sqrt x s = s if s*s <= x
sqrt x s = sqrt x (s-1) if s*s > x
- sqrt 10 5;
> 3 : int
~~~~

3- Find the sum of the squares of the first n integers n2+(n−1)2+(n−2)2+…12n2+(n−1)2+(n−2)2+…12.  
* The sum of the squares of the first 0 integers is 0.  
* The sum of the squares of the first n integers is n squared plus the sum of the squares of the first n-1 integers.  
~~~~
- sumSq 3;
> 14 : int
~~~~

4- Find the sum of the halves of the first n integers n/2+(n−1)/2…+1/2n/2+(n−1)/2…+1/2.
~~~~
- sumHalf 6;
> 9 : int
~~~~

5- Find the sum of applying function f to the first n integers.  
* The sum of applying f to the first 0 integers is 0.  
* The sum of applying f to the first n integers is f applied to n plus the sum of applying f to the first n-1 integers.
~~~~
- fun inc x = x+1;
> val inc = fn : int -> int
- sumF inc 3;
> 9 : int i.e. inc 3+inc 2+ inc 1+ 0
~~~~

6- Write sumSq using sumF.

7- Write sumHalf using sumF.

## Question C (Lists).

1- Write a function to drop the first n elements of a list l: 
~~~~
drop n l : int -> a' list -> a' list  
drop 3 [1,2,3,4,5] ==> [4,5]
~~~~
* To drop 0 elements from a list return the list.
* To drop n elements from the empty list, return the empty list.
* To drop n elements from a list, drop n-1 elements from the tail.

2- Write a function to take the first n elements of a list l: 
~~~~
take n l : int -> 'a list -> 'a 
take 3 ["a","b","c","d","e"] ==> ["a","b","c"]
~~~~
* To take 0 elements from a list return the empty list.
* To take n elements from the empty list, return the empty list.
* To take elements from a list, put the head of the list onto the result of taking n-1 elements from the tail.

3- Write a function to check if list l1 starts list l2: 
~~~~
starts l1 l2 : ''a list -> ''a list -> bool  
starts [1,2,3] [1,2,3,4] ==> true
~~~~
* An empty list starts a list.
* A list does not start an empty list.
* A list starts a second list if they have same head and the tail of the first starts the tail of the second.

4- Write a function to check if list l1 is contained in list l2: 
~~~~
contains l1 l2 : ''a list -> ''a list -> bool
contains ["d","e","f"] ["a","b","c","d","e","f","g","h"] ==> true
~~~~
* A list is not contained in an empty list.
* A list is contained in a second list if it starts the second list.
* Otherwise, a list is contained in a second list if it is contained in the tail of the second list.

5- Write a function to delete a list from another list: 
~~~~
delete l1 l2 : ''a list -> ''a list -> ''a list 
delete [3,4,5] [1,2,3,4,5,6] ==> [1,2,6]
~~~~
* To delete a list from the empty list, return the empty list.
* To delete a list from a second list, if the first list starts the second list then drop the length of the first list from the second list.
* Otherwise, put the head of the second list onto the result of deleting the first list from the tail of the second.

6- Write a function to delete every occurrence of a list from another list:
~~~~
deleteAll l1 l2 : ''a list ->''a list -> ''a list
deleteAll [1,2,3] [3,2,1,2,3,2,1,2,3] ==> [3,2,2]
~~~~
* All occurrences have been deleted from an empty list.
* If the first list starts the second list, delete it and then delete all occurrences in the remaining list.
* Otherwise, put the head of the second list on the front of deleting all occurrences of the first list in the tail.

## Question D (Essay-style, functional programming).

1- Explain recursion.
2- Explain tail recursion and how it differs from plain old recursion. If you want to write efficient code, which is better, and why?
3- Explain the Church-Rosser property, and how it is relevant to programming language execution.
4- The cost of running a calculation is calculated as follows: programmercosts+computingcosts=totalcostsprogrammercosts+computingcosts=totalcosts. A more detailed equation is designcosts+programmercosts+debuggingcosts+computingcosts=totalcostsdesigncosts+programmercosts+debuggingcosts+computingcosts=totalcosts. With these equations in mind, describe some of the trade-offs involved in choosing a programming language for an embedded chip in a car versus an Android app.
5- “Pure functional programming has no global state.”
Explain what this assertion means.
Give one advantage and one disadvantage of using a language without global state.
6- Explain the different optimisations possible in imperative versus declarative programming, and the implications for space and time efficiency and development cost.
