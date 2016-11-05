(* ==== Question G === *)

(* 1 - Represent a binary number as a list of booleans, where the first boolean *)
(* is the least significant digit. Thus, [false,true] represents two and        *)   
(* [false,true,false,true] represents ten. Recall the school algorithm for      *)
(* addition, involving carrying ones over to more significant digits as         *)
(*  appropriate. Implement this binary addition as a function of type bool      *)
(* list -> bool list -> bool list.                                              *)
fun binAdd [] [] = []
  | binAdd [] x = x
  | binAdd x [] = x
  | binAdd (hd1::tl1) (hd2::tl2) = 
    if (hd1 andalso hd2) 
      then false::(binAdd (hd1::tl1) tl2)
    else (hd1 orelse hd2)::(binAdd tl1 tl2);

(* 2 - Using an accumulator variable or otherwise, write a function max of      *)
(* type int list -> int that returns the greatest element of its input.         *)
fun max (hd::tl) = 
  let fun anyhigher n [] = n
        | anyhigher n (hd::tl) =
            if (hd > n)
              then anyhigher hd tl
            else anyhigher n tl
  in
    anyhigher hd tl
  end;

(* 3 - Using accumulator variables or otherwise, write a function avg of type   *)
(* real list -> real that returns the average of a list.                        *)

fun avg numbers =
  let fun sum [] = 0
        | sum (hd::tl) = hd + (sum tl)
  in
   (* (sum numbers) / (Real.fromInt (length numbers)) *)
    sum [1,2,3,4]
  end;
