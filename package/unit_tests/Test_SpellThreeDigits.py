import unittest
from ..integerSpeller import integerSpeller


class Test_SpellThreeDigits(unittest.TestCase):

    instance = integerSpeller()
    
    def test_zero(self):
        self.assertEqual(self.instance.spellThreeDigits(0), "zero")
        
    def test_four(self):
        self.assertEqual(self.instance.spellThreeDigits(4), "four")
        
    def test_nine(self):
        self.assertEqual(self.instance.spellThreeDigits(9), "nine")
        
    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.spellThreeDigits(-1)
            
        with self.assertRaises(ValueError):
            self.instance.spellThreeDigits(1000)
            
        with self.assertRaises(ValueError):
            self.instance.spellThreeDigits(435153)
            
    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
        # self.assertEqual(self.instance.spellThreeDigits(01), "one")
        
    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.spellThreeDigits("23")
            
        with self.assertRaises(TypeError):
            self.instance.spellThreeDigits(77.0)
            
        with self.assertRaises(TypeError):
            self.instance.spellThreeDigits(35.5)
            
    def test_ten(self):
        self.assertEqual(self.instance.spellThreeDigits(10), "ten")
        
    def test_sixteen(self):
        self.assertEqual(self.instance.spellThreeDigits(16), "sixteen")
        
    def test_twenty(self):
        self.assertEqual(self.instance.spellThreeDigits(20), "twenty")
        
    def test_thirty_two(self):
        self.assertEqual(self.instance.spellThreeDigits(32), "thirty-two")
        
    def test_eighty_eight(self):
        self.assertEqual(self.instance.spellThreeDigits(88), "eighty-eight")
        
    def test_two_thirty_six(self):
        self.assertEqual(self.instance.spellThreeDigits(236), "two hundred thirty-six")
        
    def test_nine_ninety_nine(self):
        self.assertEqual(self.instance.spellThreeDigits(999), "nine hundred ninety-nine")
        
    def test_six_hundred(self):
        self.assertEqual(self.instance.spellThreeDigits(600), "six hundred")
            
            
if __name__ == "__main__":
    unittest.main()