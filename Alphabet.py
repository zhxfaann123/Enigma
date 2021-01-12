class Alphabet:
    """
    The alphabet of encodable characters. Each character has two presentations:
    the raw character of its index(started with 0).
    """

    def __init__(self, *self_defined_alphabet):
        self.alphabetString = self_defined_alphabet[0]

    def size(self):
        """
        :return: The length of the alphabetString
        """
        # FIXME

    def contains(self, item):
        """
        Return True iff the character is in the alphabet; otherwise return False
        """
        # FIXME

    def toChar(self, index):
        """
        convert an Integer(the index of a character in the alphabet) to its corresponding character
        """
        # FIXME

    def toInt(self, char):
        """
        convert a character to its index in the alphabet
        """
        # FIXME
