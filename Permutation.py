from io import StringIO
from Alphabet import Alphabet
from Utils import Default_Alphabet_String


class Permutation:
    def __init__(self, cycles, alphabet: Alphabet):
        # FIXME

    def permute(self, input):
        # FIXME

    def invert(self, input):
        # FIXME

    def size(self):
        return self._alphabet.size()

    def warp(self, p):
        r = p % self.size()
        if r < 0:
            r += self.size()
        return r

    # FIXME: ADDITIONAL METHOD, IF NEEDED









