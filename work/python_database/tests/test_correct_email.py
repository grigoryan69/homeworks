import unittest
import unittest.mock
import sys

sys.path.append('..')
sys.path.insert(0, './application')

from database import correct_email


class TestContainsNumber(unittest.TestCase):
    # Positive Tests
    def test_gmail_com(self):
        self.assertEqual(correct_email('dave69tv@gmail.com'), 'dave69tv@gmail.com')

    def test_mail_ru(self):
        self.assertEqual(correct_email('teacher@mail.ru'), 'teacher@mail.ru')

    def test_yandex_ru(self):
        self.assertEqual(correct_email('student@yandex.ru'), 'student@yandex.ru')

    # Negative Tests
    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_only_letters(self, mock):
        self.assertEqual(correct_email('dave'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_only_numbers(self, mock):
        self.assertEqual(correct_email('1231'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_symbols(self, mock):
        self.assertEqual(correct_email('^%&$'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_letters_and_numbers(self, mock):
        self.assertEqual(correct_email('abc123'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_letters_and_symbols(self, mock):
        self.assertEqual(correct_email('abc#@$'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_symbols_and_numbers(self, mock):
        self.assertEqual(correct_email('$%$#^16516'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_nothing_was_entered(self, mock):
        self.assertEqual(correct_email(''), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_backspace_was_entered(self, mock):
        self.assertEqual(correct_email(' '), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_letters_after_at(self, mock):
        self.assertEqual(correct_email('something@asdgdsf'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_numbers_after_at(self, mock):
        self.assertEqual(correct_email('something@1234'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_symbols_after_at(self, mock):
        self.assertEqual(correct_email('input@^%&$'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_letters_and_numbers_after_at(self, mock):
        self.assertEqual(correct_email('else@abc123'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_letters_and_symbols_after_at(self, mock):
        self.assertEqual(correct_email('another@abc#@$'), False)

    @unittest.mock.patch('builtins.input', side_effect=[False])
    def test_symbols_and_numbers_after_at(self, mock):
        self.assertEqual(correct_email('test@$%$#^16516'), False)


if __name__ == '__main__':
    unittest.main()
