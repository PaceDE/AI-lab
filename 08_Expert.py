animal(dog) :- is_true("has fur"), is_true("says woof").  
animal(cat) :- is_true("has fur"), is_true("says meow").  
animal(duck) :- is_true("has feathers"), is_true("says quack"). 
 
is_true(Q) :-  
format("~s?\n", [Q]), 
read(yes) 