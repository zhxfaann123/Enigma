import unittest
from io import StringIO
from _io import TextIOWrapper
from Alphabet import Alphabet
from Permutation import Permutation
from FixedRotor import FixedRotor
from Utils import *


class MyTestCase(unittest.TestCase):

    def test_alphabet(self):
        alphabet = Alphabet(Default_Alphabet_String)
        self.assertEqual(alphabet.size(), 26)
        self.assertEqual(alphabet.toInt('A'), 0)
        self.assertEqual(alphabet.toChar(0), 'A')
        self.assertEqual(alphabet.toInt('Z'), 25)
        self.assertEqual(alphabet.toChar(25), 'Z')

    def test_permutation(self):
        cycle = "(AELTPHQXRU) (BKNW) (CMOY) (DFG) (IV) (JZ) (S)"
        alphabet = Alphabet(Default_Alphabet_String)
        permutation = Permutation(cycle, alphabet)
        self.assertEqual(permutation.permute('A'), 'E')
        self.assertEqual(permutation.invert('E'), 'A')
        self.assertEqual(permutation.permute('S'), 'S')
        self.assertEqual(permutation.invert('S'), 'S')

    def test_advance(self):
        alphabet = Alphabet("ABCD")
        cycle = "(ABCD)"
        permutation = Permutation(cycle, alphabet)
        fix_rotor = FixedRotor("fix", permutation)
        self.assertEqual(fix_rotor.convertForward(0), 1)
        self.assertEqual(fix_rotor.convertBackward(1), 0)


if __name__ == '__main__':
    unittest.main()
