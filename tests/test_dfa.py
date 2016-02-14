from autamata.dfa import DFA
from autamata.transition import TransitionTable

def test_consume():

    alphabet = ["a", "b"]
    states = ["1", "2"]

    table = TransitionTable(alphabet, states)
    table.add_transition("a", "2", "2")
    table.add_transition("b", "2", "2")
    table.add_transition("a", "1", "2")
    table.add_transition("b", "1", "1")

    dfa = DFA(table)

    accepted = dfa.consume("ba")
    assert accepted, "'ba' is expected to be accepted."

    accepted = dfa.consume("babbb")
    assert accepted, "'babbb' is expected to be accepted."    

    accepted = dfa.consume("b")
    assert not accepted, "'b' is expected not to be accepted."

    accepted = dfa.consume("bbb")
    assert not accepted, "'bbb' is expected not to be accepted."