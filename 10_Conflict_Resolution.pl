rule1(climate_change).
rule2(climate_change).

conflict(X) :- rule1(X), rule2(X).

% Example query:
% ?- conflict(climate_change).
% Expected answer: true.
