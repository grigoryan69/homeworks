import unittest
from database import correct_email

class Unit(unittest.TestCase):

    def test1(self):
        result = correct_email('nune')
        self.assertEqual(result, 0)

if __name__ == '__main__': 
    unittest.main()
