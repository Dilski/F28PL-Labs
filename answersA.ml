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
