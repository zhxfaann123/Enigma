from Alphabet import Alphabet
from Reflector import Reflector
from Permutation import Permutation
from Utils import *


class Machine:
    """
    The Enigma Machine, consisting several rotors(Reflector/FixRotor/MovingRotor)
    """
    def __init__(self, alphabet: Alphabet, num_rotors: int, num_pawls: int, rotors: list):
        self._alphabet = alphabet
        # FIXME

    def convert_char(self, c: int):
        """
        Return the result of converting the input character c(in the form of an integer)
        """
        # FIXME

    def convert_str(self, msg: str):
        """
        Returns the encoding of msg, updating the state of the rotors accordingly.
        """
        # FIXME

    def num_rotors(self):
        return 0  # FIXME

    def num_pawls(self):
        return 0  # FIXME

    def set_rotors(self, setting: str):
        # FIXME

    def set_plugboard(self, cycles: str):
        # FIXME

    # FIXME: ADDITIONAL METHOD HERE, IF NEEDED
