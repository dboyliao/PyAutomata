
from .exceptions import DeadState, InvalidTransition

class TransitionTable(object):
    """
    Transition table
    """

    def __init__(self, alphabet, states, start_state = None, final_state = None):

        self.alphabet = alphabet
        self.states = states

        if start_state is not None and not start_state in states:
            raise ValueError("start state is invalid: {}".format(start_state))

        if final_state is not None and not final_state in states:
            raise ValueError("final state is invalid: {}".format(final_state))

        if start_state is None:
            self.__start_state = states[0]
        else:
            self.__start_state = start_state

        if final_state is None:
            self.__final_state = states[-1]
        else:
            self.__final_state = final_state

        self.__rules = {}

    @property
    def start_state(self):
        return self.__start_state

    @start_state.setter
    def start_state(self, new_value):
        raise ValueError("start_state is a read-only attribute.")

    @property
    def final_state(self):
        return self.__final_state

    @final_state.setter
    def final_state(self):
        raise ValueError("final_state is a read-only attribute.")

    @property
    def rules(self):

        return self.__rules


    @rules.setter
    def rules(self, new_value):

        raise ValueError("`rules` is a read-only property.")


    def add_transition(self, input_symbol, current_state, output_state):

        self.__rules[(input_symbol, current_state)] = output_state


    def __is_valid(self, input_symbol, current_state):

        ret_value = True

        if not input_symbol in self.alphabet or not current_state in self.states:
            ret_value = False

        return ret_value

    def consume(self, input_symbol, current_state):

        if not self.__is_valid(input_symbol, current_state):
            raise InvalidTransition("Invalid symbol or state: ({}, {})".format(input_symbol, current_state))

        if not (input_symbol, current_state) in self.rules:

            raise DeadState("transition rule not defined for ({}, {})".format(input_symbol, current_state))
        else:

            return self.rules[(input_symbol, current_state)]


    def __str__(self):

        format = "(input:{}, current state:{}) --> {}\n"
        ret_string = "alphabet: {}\nstates: {}\n".format(self.alphabet, self.states)

        for (input_symbol, current_state), output_state in self.rules.items():

            ret_string += format.format(input_symbol, current_state, output_state)

        return ret_string