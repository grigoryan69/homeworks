import unittest
from email import correct_email

class Unit(unittest.TestCase):

    def test1(self):
        result = correct_email('nune')
        self.assertEqual(result, 0)
    
    def test2(self):
        result = correct_email('arusik@12123')
        self.assertEqual(result, 0)

    def test3(self):
        result = correct_email('nune@gmail')
        self.assertEqual(result, 0)    

    def test4(self):
        result = correct_email('arusik@.com')
        self.assertEqual(result, 0)     

    def test5(self):
        result = correct_email('davo@something.com')
        self.assertEqual(result, 0)

    def test6(self):
        result = correct_email('arusikgmail.com')
        self.assertEqual(result, 0)   

    def test7(self):
        result = correct_email('dave69tv@gmail.com')
        self.assertEqual(result, 'dave69tv@gmail.com')

    def test8(self):
        result = correct_email('dave69tv@yandex.ru')
        self.assertEqual(result, 'dave69tv@yandex.ru')

    def test9(self):
        result = correct_email('dave69tv@mail.ru')
        self.assertEqual(result, 'dave69tv@mail.ru')

    def test10(self):
        result = correct_email('dave@mail.ru')
        self.assertEqual(result, 'dave@mail.ru')

    def test11(self):
        result = correct_email(1)
        self.assertEqual(result, 0)
        
    def test13(self):
        result = correct_email('112dsf312')
        self.assertEqual(result, 0)       

    def test14(self):
        result = correct_email('')
        self.assertEqual(result, 0)

    def test15(self):
        result = correct_email(' ')
        self.assertEqual(result, 0)

    def test17(self):
        result = correct_email(True)
        self.assertEqual(result, 0)

    def test18(self):
        result = correct_email(False)
        self.assertEqual(result, 0)


if __name__ == '__main__': 
    unittest.main()
