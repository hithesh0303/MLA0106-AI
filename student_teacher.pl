% Student database
student(101, ram).
student(102, sita).
student(103, john).

% Teacher database
teacher(t1, smith).
teacher(t2, david).
teacher(t3, scott).

% Subject database with subject code
subject(cs101, ai).
subject(cs102, dbms).
subject(cs103, networks).

% Teacher teaches subject
teaches(smith, ai).
teaches(david, dbms).
teaches(scott, networks).

% Student studies subject
studies(ram, ai).
studies(sita, dbms).
studies(john, networks).

% Rule: find teacher of a student
student_teacher(Student, Teacher):-
    studies(Student, Subject),
    teaches(Teacher, Subject).

% Rule: find subject code of student
student_subject_code(Student, Code):-
    studies(Student, Subject),
    subject(Code, Subject).
