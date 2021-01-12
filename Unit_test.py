import unittest
from io import StringIO
from _io import TextIOWrapper


def test_io_func(file_d: TextIOWrapper):
    print(file_d.read())


class MyTestCase(unittest.TestCase):
    def test_string_reader(self):
        a = 1
        assert a == 1


if __name__ == '__main__':
    unittest.main()
