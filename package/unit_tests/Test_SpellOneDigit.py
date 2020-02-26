import unittest
from ..integerSpeller import integerSpeller


class Test_SpellOneDigit(unittest.TestCase):

    instance = integerSpeller()
    
    def test_zero(self):
        self.assertEqual(self.instance.spellOneDigit(0), "zero")
        
    def test_four(self):
        self.assertEqual(self.instance.spellOneDigit(4), "four")
        
    def test_nine(self):
        self.assertEqual(self.instance.spellOneDigit(9), "nine")
        
    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.spellOneDigit(-1)
            
        with self.assertRaises(ValueError):
            self.instance.spellOneDigit(10)
            
        with self.assertRaises(ValueError):
            self.instance.spellOneDigit(55)
            
    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
        # self.assertEqual(self.instance.spellOneDigit(01), "one")
        
    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.spellOneDigit("2")
            
        with self.assertRaises(TypeError):
            self.instance.spellOneDigit(7.0)
            
        with self.assertRaises(TypeError):
            self.instance.spellOneDigit(5.5)
            
            
if __name__ == "__main__":
    unittest.main()