import unittest
from get_juft import get_even

class JuftCheck(unittest.TestCase):
    def juftchecker(self):
        formatted_list = get_even([1,2,3,4,5,6,7,8,9,20,34,230,23])
        self.assertListEqual(formatted_list, [2,4,6,8,20,34,230])

unittest.main()