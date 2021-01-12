from Alphabet import Alphabet
from Permutation import Permutation


class Rotor:
    def __init__(self, name, perm: Permutation):
        self._name = name
        self._perm = perm
        self._cPos = 'a'
        self._iPos = 1

    def name(self):
        return self._name

    @staticmethod
    def rotates():
        """
        Return True iff the rotor can rotate
        """
        return False

    @staticmethod
    def reflecting():
        """
        Return True iff the rotor is a Reflector
        """
        return False

    @staticmethod
    def setting():
        """
        Return the setting of the rotor
        """
        return 0

    def set(self, cposn):
        """
        set setting() to cposn
        """
        # FIXME

    def convertForward(self, p):
        """
        Return the conversion of P (an integer in the range 0 ... size() - 1)
        according to the permutation of the rotor
        """
        # FIXME

    def convertBackward(self, e):
        """
        Return the conversion of P (an integer in the range 0 ... size() - 1)
        according to the inverse of the permutation of the rotor
        """
        # FIXME

    @staticmethod
    def atNotch():
        """
        Return true iff the rotor is at the notch (for moving rotor only)
        """
        return False

    # FIXME: ADDITIONAL METHOD HERE, IF NEEDED
