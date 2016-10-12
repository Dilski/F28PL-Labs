(* == Question A == *)

(* 1 -Multiply real x by integer y to give a real. *)
fun realIntMult (x:real) (y:int) = x * real y;

(* 2 - Check if string s1 has more letters than string s2 *)
fun moreLetters (s1:string) (s2:string) = s1 > s2;

(* 3 - Check if character c represents a digit *)
fun isDigit(c:char) = #"0" <= c andalso c <= #"9";

(* 4 - If character c represents a digit then return its integer equivalent; otherwise return ~1 *)
fun digitValue (c:char) =
  if (c <= #"9" andalso #"0" <= c)
  then valOf (Int.fromString (Char.toString c))
  else ~1;

(* 5 - Convert a real r into a tuple of its value and integer equivalent *) 
fun conv (r:real) = (r, (floor r));

(* 6 - Implement the NAND function *)
fun NAND (x:bool) (y:bool) = ((x<>y)=true);

(* == Question B == *)

(* 1 - Find the integer logarithm to the base 2 of an integer n by repeatedly dividing by 2 and counting *)
fun log2 1 = 0
  | log2 n = 1+log2 (n div 2);

(* 2 - Find the square root of an integer x by repeatedly decrementing an initial guess s *)
fun sqrt x s =
  if (s*s <=x) then s
  else sqrt x (s-1);

(* 3 - Find the sum of the squares of the first n integers *)
fun sumSq 0 = 0
  | sumSq n = n*n + (sumSq(n-1));

(* 4 - Find the sum of the halves of the first n integers *)
fun sumHalf 0 = 0
  | sumHalf n = floor(Real.fromInt(n)/2.0) + sumHalf(n-1);

(* 5 - Find the sum of applying function f to the first n integers *)
fun sumF f 0 = 0
  | sumF f n = (f n) + (sumF f (n-1));

(* 6 - Write sumSq using sumF. *)
fun sumSqF n = sumF (fn x => x*x) n; 

(* 7 - Write sumHalf using sumF *)
fun fSumHalf n = sumF (fn x => floor(Real.fromInt(n)/2.0)) n;

(* == Question C == *)

(* 1 - Write a function to drop the first n elements of a list *)
fun drop 0 l = l
  | drop n l = tl (drop (n-1) l);

(* 2 - Write a function to take the first n elements of a list l *);
fun take 0 l = []
  | take n l = hd(l)::(take (n-1) (tl l)) ;

(* 3 - Write a function to check if list l1 starts list l2 *)
fun starts [] l2 = true
  | starts l1 [] = false
  | starts l1 l2 = (((hd l1) = (hd l2)) andalso (starts (tl l1) (tl l2)));
    
(*4 Write a function to check if list l1 is contained in list l2: *)
(* fun contains l1 l2 =
	if (l2=[]) then false
  else if l1=l2 then true
	else false;
*)
(* 5 Write a function to delete a list from another list *)
fun delete l1 [] = []
  | delete l1 l2 = if starts l1 l2 then drop (length l1) l2 else (hd l2)::(delete l1(tl l2)) ;




