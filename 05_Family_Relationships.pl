parent(john, mary).
parent(mary, susan).
parent(john, mike).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Example query:
% ?- grandparent(john, susan).
% Expected answer: true.
