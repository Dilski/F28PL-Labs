(* Quick Sort *) 
fun quickSplitter [] mid left right       = (left, right)
  | quickSplitter (hd::tl) mid left right = 
      if hd <= mid then 
        quickSplitter tl mid (left@[hd]) right
      else
        quickSplitter tl mid left (right@[hd]);


fun quickSort []       = []
  | quickSort (hd::tl) = 
      let
        val (l, r) = quickSplitter tl hd [] []
      in
        quickSort l @ [hd] @ quickSort r
      end;

(* Bubble sort *)
fun bblSort [] = []
  | bblSort [a] = [a]
  | bblSort (hd1::hd2::tl) =
      if hd1 > hd2 then
        hd2::(bblSort (hd1::tl))
      else
        hd1::(bblSort (hd2::tl));

fun bubbleSort [] = []
  | bubbleSort (hd::tl) = bblSort (hd::(bubbleSort tl));


