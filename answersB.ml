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
