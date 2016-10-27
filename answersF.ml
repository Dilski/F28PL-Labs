(* == Question F == *)

(* 1 - Write a function to remove all the non-letters off the front of a list of characters *)
fun strip [] = []
  | strip (hd::tl) = 
      if (#"a" <= hd andalso hd <= #"z") orelse (#"A" <= hd andalso hd <= #"Z") 
        then hd::tl 
      else strip tl;

strip [#".",#" ",#"t",#"h",#"e"];

(* 2 - Write a function to take the next word off a list of characters. The function returns a tuple of the word as a list of characters and the rest of the list. *)
fun next [] = ([],[])
  | next (hd::tl) = 
      let 
        fun isletter hd = (#"a" <= hd andalso hd <= #"z") orelse (#"A" <= hd andalso hd <= #"Z");
        fun nextWord ([], []) = ([], [])
          | nextWord (x, []) = (x, [])
          | nextWord (x, (hd::tl)) = 
               if not (isletter hd)
                  then (x, (hd::tl))
                else nextWord(x@[hd], tl);
      in 
        if (isletter hd)
          then nextWord([], (hd::tl)) 
        else ([], (hd::tl)) 
      end;

next [#"t",#"h",#"e",#" ",#"c",#"a",#"t"];

(* 3 - Write a function to turn a list of characters into a list of individual words as strings *)

fun words [] = []
  | words l1 = 
     let 
       fun impList ([],[]) = ([],[])
         | impList (l1,[]) = (l1,[])
         | impList (l1,l2) = (impList (l1@[(String.implode (#1 (next (strip l2))))], (#2 (next (strip l2)))))
     in 
       #1 (impList ([], l1)) 
     end;

words [#"t",#"h",#"e",#" ",#"c",#"a",#"t"];

(* 4 - Write a function to increment the count for a word in a list of words and counts. *)

fun incCount word [] = [(word,1)]
  | incCount word (hd::tl) =
    if ((#1 hd)=word) 
      then (word, (#2 hd) +1)::tl
    else hd::(incCount word tl);

incCount "late" (incCount "very" [("im",1),("here",1),("very",2)]);

(* 5 - Write a function which given a list of words and an empty list, constructs the frequency count list. *)
fun counts [] countList = countList
  | counts (hd::tl) [] = counts tl (incCount hd [])
  | counts (hd::tl) countList = counts tl (incCount hd countList);

counts ["the","cat","sat","on","the","mat"] [];

