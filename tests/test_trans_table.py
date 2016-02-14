from autamata.transition import TransitionTable
from autamata.exceptions import DeadState, InvalidTransition
import sys

def get_table(alphabet, states):

    return TransitionTable(alphabet, states)

def test_init():

    alphabet = ["a", "b", "c", "d"]
    states = ["1", "2", "3"]

    table = get_table(alphabet, states)

    assert table.start_state == "1", "The start state should be '1', get {}".format(table.start_state)
    assert table.final_state == "3", "The final state should be '3', get {}".format(table.final_state)

def test_add_transition_rule():
    alphabet = ["a", "b", "c", "d"]
    states = ["1", "2", "3"]

    table = get_table(alphabet, states)

    table.add_transition("a", "1", "2")

    assert ("a", "1") in table.rules, "rule for ('a', '1') is not defined."
    assert table.rules[("a", "1")] == "2", "rule for ('a', '1') is {}, expect '2'".format(table.rules[("a", "1")])


def test_consume():

    alphabet = ["a", "b", "c", "d"]
    states = ["1", "2", "3"]

    table = TransitionTable(alphabet, states)

    table.add_transition("a", "1", "2")
    table.add_transition("b", "1", "3")
    table.add_transition("c", "1", "1")

    next_state = table.consume("a", "1")

    assert next_state == "2", "expect '2', get {}".format(next_state)

    next_state = table.consume("b", "1")

    assert next_state == "3", "expect '3', get {}".format(next_state)

    # test InvalidTransition
    try:
        # invalid symbol
        table.consume("q", "1")
    except InvalidTransition:
        pass

    try:
        # invalid state
        table.consume("a", "4")
    except InvalidTransition:
        pass

    # testing DeadSate
    try:
        table.consume("d", "1")
    except DeadState:
        pass


def test_print():
    alphabet = ["a", "b", "c", "d"]
    states = ["1", "2", "3"]

    table = TransitionTable(alphabet, states)

    table.add_transition("a", "1", "2")
    table.add_transition("b", "1", "3")
    table.add_transition("c", "1", "1")
    table.add_transition("d", "1", "1")

    print >> sys.stderr, "\n"
    print >> sys.stderr, table