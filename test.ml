fun testFunction l n f r =
  if f = r then ("Question " ^ l ^ ", number " ^ n ^ ": PASS")
  else ("Question " ^ l ^ ", number " ^ n ^ ": FAIL");

fun assertsTrue f q n =
  if (f = true) then ("Question " ^ q ^ ", number " ^ n ^ ": PASS")
  else ("Question " ^ q ^ ", number " ^ n ^ ": FAIL");

fun assertsFalse f q n =
  if (f = false) then ("Question " ^ q ^ ", number " ^ n ^ ": PASS")
  else ("Question " ^ q ^ ", number " ^ n ^ ": FAIL");

use "answers.ml";

(* A 1 *)
realIntMult 3.3 3;
(* A 2 *)
assertsFalse (moreLetters "big" "small") "A" "2";
(* A 3 *)
assertsTrue (isDigit #"7") "A" "3";
(* A 4 *)
digitValue #"a";
digitValue #"7";
(* A 5 *)
conv 99.99;
(* A 6 *)
assertsTrue (NAND false true) "A" "6";
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
assertsTrue (starts [1,2,3] [1,2,3,4]) "C" "3";



