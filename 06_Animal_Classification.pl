has_hair(tiger).
gives_milk(tiger).

mammal(X) :- has_hair(X), gives_milk(X).

% Example query:
% ?- mammal(tiger).
% Expected answer: true.
