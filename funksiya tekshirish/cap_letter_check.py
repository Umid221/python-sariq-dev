import unittest
from cap_letter import cap_letter

class CapCheck(unittest.TestCase):
    def capchecker(self):
        formatted_name = cap_letter(['salom', 'ahvollar qalay'])
        self.assertListEqual(formatted_name, ['Salom', "Ahvollar qalay"])

unittest.main()