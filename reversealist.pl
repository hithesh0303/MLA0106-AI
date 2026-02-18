append([],L,L).
append([H|T],L,[H|R]):-
    append(T,L,R).

reverse([],[]).
reverse([H|T],R):-
    reverse(T,RT),
    append(RT,[H],R).
