import unittest
import sys 

sys.path.insert(1, 'final_project/machinetranslation/translator.py')

from machinetranslation.translator import english_to_french
from machinetranslation.translator import french_to_english

class TestStringMethods(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('hello'), 'hello')
        self.assertIsNone(english_to_french(None))

    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        self.assertIsNone(french_to_english(None))

if __name__ == '__main__':
    unittest.main()