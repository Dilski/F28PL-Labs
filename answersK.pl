/** <module> Question K
@author Dillon Fearns <djf1@hw.ac.uk>

*/

person(jake).
person(jill).
person(john).
person(joan).

likes(jake,tomato).
likes(jill,cheese).
likes(jill,tomato).
likes(john,cheese).
likes(joan,cheese).
likes(joan,tomato).
likes(X,pizza) :- likes(X,cheese), likes(X,tomato).

knows(jake,jill).
knows(jill,john).
knows(john,joan).
knows(joan,jake).
knows(X,X).

knowslikespizza(X,Y) :- knows(X,Y), likes(Y,pizza).

place(aberdeen).
place(dundee).
place(edinburgh).
place(glasgow).
place(kirkcaldy).
place(stAndrews).

between(aberdeen,dundee,60).	
between(dundee,edinburgh,60).
between(stAndrews,edinburgh,45).
between(dundee,stAndrews,10).
between(dundee,aberdeen,60).
between(stAndrews,kirkcaldy,30).
between(kirkcaldy,edinburgh,35).
between(glasgow,edinburgh,45).
between(X,Y,Z) :- between(Y,X,Z).
between(X,Y,Z).
between(X,Y,Z) :- between(X,Q,Z1),
		  between(Q,Y,Z2), 
                  Z is Z1 + Z2.

