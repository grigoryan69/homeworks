import unittest
import sys

sys.path.append('..')
sys.path.insert(0, './application')

from database import contains_number


class TestContainsNumber(unittest.TestCase):
    # Positive Tests
    def test_numbers_only(self):
        self.assertEqual(contains_number('0101'), True)

    def test_numbers_and_letters(self):
        self.assertEqual(contains_number('9894abc'), True)

    def test_numbers_and_symbols(self):
        self.assertEqual(contains_number('989pyt4&*@'), True)

    # Negative Tests
    def test_letters(self):
        self.assertEqual(contains_number('abcd'), False)

    def test_symbols(self):
        self.assertEqual(contains_number('*%^*'), False)

    def test_letters_and_symbols(self):
        self.assertEqual(contains_number('some&*('), False)

    def test_empty_argument(self):
        self.assertEqual(contains_number(''), False)

    def test_backspace(self):
        self.assertEqual(contains_number(' '), False)


if __name__ == '__main__':
    unittest.main()
