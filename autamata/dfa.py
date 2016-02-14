
from .transition import TransitionTable
from .exceptions import DeadState

class DFA(object):

    def __init__(self, trans_table):

        self.alphabet = trans_table.alphabet
        self.__trans_table = trans_table
        self.current_state = trans_table.start_state

    @property
    def trans_table(self):
        """
        The transition table
        """
        return self.__trans_table

    @trans_table.setter
    def trans_table(self, new_value):
        if not isinstance(new_value, TransitionTable):
            raise ValueError("an instance of TransitionTable expected, get {}".format(type(new_value)))

        self.__trans_table = new_value


    def consume(self, string):

        accepted = True

        for s in string:
            try:
                self.current_state = self.trans_table.consume(s, self.current_state)

            except DeadState, InvalidTransition:
                return False

        if not self.current_state == self.trans_table.final_state:
            accepted = False
        
        self.current_state = self.trans_table.start_state

        return accepted

