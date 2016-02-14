## `automata` - A Simple Python Package for Playing with Automata

## Deterministic Finite Automata

```{python}
from automata.dfa import DFA
from automata.transition import TransitionTable

alphabet = ["a", "b"]
states = ["1", "2"]
table = TransitionTable(alphabet, states)
table.add_transition("b", "2", "2")
table.add_transition("a", "1", "2")
table.add_transition("b", "1", "1")

dfa = DFA(table)

accepted = dfa.consume("bba")

if accepted:
    print "'bba' is accepted."
else:
    print "'bba' is not accepted."
```

## Install

- run `make install` to install dependencies for this package.
- see `requirements.txt` for required packages.

## Test

1. run `make test` to run the tests.
    - run `make install` first to install the packages required for testing. 
2. see the result of the tests in `tests/reports/index.html`.