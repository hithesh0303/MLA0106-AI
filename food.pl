likes(john, pizza).
likes(mary, burger).
likes(sam, pizza).

friend(X,Y) :- likes(X,Z), likes(Y,Z).
