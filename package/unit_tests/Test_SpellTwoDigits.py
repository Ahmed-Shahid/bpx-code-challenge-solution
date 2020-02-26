import unittest
from ..integerSpeller import integerSpeller


class Test_SpellTwoDigits(unittest.TestCase):

    instance = integerSpeller()
    
    def test_zero(self):
        self.assertEqual(self.instance.spellTwoDigits(0), "zero")
        
    def test_four(self):
        self.assertEqual(self.instance.spellTwoDigits(4), "four")
        
    def test_nine(self):
        self.assertEqual(self.instance.spellTwoDigits(9), "nine")
        
    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.spellTwoDigits(-1)
            
        with self.assertRaises(ValueError):
            self.instance.spellTwoDigits(100)
            
        with self.assertRaises(ValueError):
            self.instance.spellTwoDigits(450)
            
    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
        # self.assertEqual(self.instance.spellTwoDigits(01), "one")
        
    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.spellTwoDigits("23")
            
        with self.assertRaises(TypeError):
            self.instance.spellTwoDigits(77.0)
            
        with self.assertRaises(TypeError):
            self.instance.spellTwoDigits(35.5)
            
    def test_ten(self):
        self.assertEqual(self.instance.spellTwoDigits(10), "ten")
        
    def test_sixteen(self):
        self.assertEqual(self.instance.spellTwoDigits(16), "sixteen")
        
    def test_twenty(self):
        self.assertEqual(self.instance.spellTwoDigits(20), "twenty")
        
    def test_thirty_two(self):
        self.assertEqual(self.instance.spellTwoDigits(32), "thirty-two")
        
    def test_eighty_eight(self):
        self.assertEqual(self.instance.spellTwoDigits(88), "eighty-eight")
            
            
if __name__ == "__main__":
    unittest.main()