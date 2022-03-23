import unittest
import unittest.mock
import sys

sys.path.append('..')
sys.path.insert(0, './application')

from database import correct_name


class TestContainsNumber(unittest.TestCase):
    # Positive Tests
    def test_many_letters(self):
        self.assertEqual(correct_name('David'), 'David')

    def test_one_letter(self):
        self.assertEqual(correct_name('L'), 'L')

    # Negative Tests
    @unittest.mock.patch('builtins.input', side_effect=[0])
    def test_backspace_was_entered(self, mock):
        pass


if __name__ == '__main__':
    unittest.main()
