fun testFunction l n f r =
  if f = r then ("Question " ^ l ^ ", number " ^ n ^ ": PASS")
  else ("Question " ^ l ^ ", number " ^ n ^ ": FAIL");

use "answers.ml";

(* A 1 *)
realIntMult 3.3 3;
(* A 2 *)
moreLetters "big" "small";
(* A 3 *)
isDigit #"7";
(* A 4 *)
digitValue #"a";
digitValue #"7";
(* A 5 *)
conv 99.99;
(* A 6 *)
NAND false true;
(* B 1 *)
log2 8;
(* B 2 *)
sqrt 10 5;
(* B 3 *)
sumSq 3;
(* B 4 *)
sumHalf 6;
(* B 5 *)
fun inc x = x+1;
sumF inc 3;
(* B 6 *)
sumF fSumSq 3;
(* B 7 *)
sumF fSumHalf 6;
(* C 1 *)
drop 3 [1,2,3,4,5];
(* C 2 *)
take 3 ["a","b","c","d","e"];
(* C 3 *)
starts [1,2,3] [1,2,3,4];

