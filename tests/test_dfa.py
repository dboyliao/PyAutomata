from automata.dfa import DFA
from automata.transition import TransitionTable

def test_set_new_transtable():

    alphabet = ["a", "b"]
    states = ["1", "2"]

    table = TransitionTable(alphabet, states)
    table.add_transition("a", "2", "2")
    table.add_transition("b", "2", "2")
    table.add_transition("a", "1", "2")
    table.add_transition("b", "1", "1")

    dfa = DFA(table)

    # invalid table
    try:
        dfa.trans_table = {}
    except ValueError:
        pass

    # new table
    new_table = TransitionTable(alphabet, states)
    new_table.add_transition("b", "2", "2")
    new_table.add_transition("a", "1", "2")
    new_table.add_transition("b", "1", "1")

    dfa.trans_table = new_table


def test_consume():

    alphabet = ["a", "b"]
    states = ["1", "2"]

    table = TransitionTable(alphabet, states)
    table.add_transition("b", "2", "2")
    table.add_transition("a", "1", "2")
    table.add_transition("b", "1", "1")

    dfa = DFA(table)

    # accepted string
    accepted = dfa.consume("ba")
    assert accepted, "'ba' is expected to be accepted."

    accepted = dfa.consume("babbb")
    assert accepted, "'babbb' is expected to be accepted."

    # not acceptable string
    accepted = dfa.consume("b")
    assert not accepted, "'b' is expected not to be accepted."

    accepted = dfa.consume("bbb")
    assert not accepted, "'bbb' is expected not to be accepted."

    # dead state
    accepted = dfa.consume("bbaba")
    assert not accepted, "'bbaba' is expected not to be accepted."

    # invalid transition
    accepted = dfa.consume("babbbc")
    assert not accepted, "'bac' is expected not to be accepted."
