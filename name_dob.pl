% Database: name and date of birth

dob(john, date(15,5,2000)).
dob(mary, date(22,8,1999)).
dob(ann, date(10,12,2001)).
dob(bob, date(3,3,1998)).

% Rule to display DOB
get_dob(Name, DOB) :-
    dob(Name, DOB).

% Rule to check if person exists
person(Name) :-
    dob(Name, _).
