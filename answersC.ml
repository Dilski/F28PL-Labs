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
 fun contains l1 l2 =
	if (l2=[]) then false
  else if l1=l2 then true
	else false;

(* 5 Write a function to delete a list from another list *)
fun delete l1 [] = []
  | delete l1 l2 = if starts l1 l2 then drop (length l1) l2 else (hd l2)::(delete l1(tl l2)) ;

(* 6 Write a function to delete every occurence of a list from another list *)
fun deleteAll l1 [] = []
  | deleteAll l1 l2 = if starts l1 l2 then deleteAll l1 (drop (length l1) l2) else (hd l2)::(deleteAll l1 (tl l2));
