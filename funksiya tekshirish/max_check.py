import unittest
from max import maximum

class MaxCheck(unittest.TestCase):
    def maximum_top(self):
        self.assertAlmostEqual(maximum(1,2,3),3)
        self.assertAlmostEqual(maximum(3,7,5),7)
        self.assertAlmostEqual(maximum(8,4,5),8)
        
unittest.main()