import unittest
from ..integerSpeller import integerSpeller


class Test_SpellInteger(unittest.TestCase):

    instance = integerSpeller()
    
    def test_zero(self):
        self.assertEqual(self.instance.spellInteger("0"), "zero")
        
    def test_four(self):
        self.assertEqual(self.instance.spellInteger("4"), "four")
        
    def test_nine(self):
        self.assertEqual(self.instance.spellInteger("9"), "nine")
        
    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.spellInteger("-1")
            
        with self.assertRaises(ValueError):
            self.instance.spellInteger("1000000000000")
            
        with self.assertRaises(ValueError):
            self.instance.spellInteger("4351534354879")
            
    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
        # self.assertEqual(self.instance.spellInteger(01), "one")
        
    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.spellInteger(23)
            
        with self.assertRaises(TypeError):
            self.instance.spellInteger(774.0)
            
        with self.assertRaises(TypeError):
            self.instance.spellInteger(3675.5)
            
    def test_ten(self):
        self.assertEqual(self.instance.spellInteger("10"), "ten")
        
    def test_sixteen(self):
        self.assertEqual(self.instance.spellInteger("16"), "sixteen")
        
    def test_twenty(self):
        self.assertEqual(self.instance.spellInteger("20"), "twenty")
        
    def test_thirty_two(self):
        self.assertEqual(self.instance.spellInteger("32"), "thirty-two")
        
    def test_eighty_eight(self):
        self.assertEqual(self.instance.spellInteger("88"), "eighty-eight")
        
    def test_two_thirty_six(self):
        self.assertEqual(self.instance.spellInteger("236"), "two hundred thirty-six")
        
    def test_nine_ninety_nine(self):
        self.assertEqual(self.instance.spellInteger("999"), "nine hundred ninety-nine")
        
    def test_six_hundred(self):
        self.assertEqual(self.instance.spellInteger("600"), "six hundred")
        
    def test_2535(self):
        self.assertEqual(self.instance.spellInteger("2535"), "two thousand five hundred thirty-five")
        
    def test_1000(self):
        self.assertEqual(self.instance.spellInteger("1000"), "one thousand")
        
    def test_5076(self):
        self.assertEqual(self.instance.spellInteger("5076"), "five thousand seventy-six")
        
    def test_111111(self):
        self.assertEqual(self.instance.spellInteger("111111"), "one hundred eleven thousand one hundred eleven")
        
    def test_100000(self):
        self.assertEqual(self.instance.spellInteger("100000"), "one hundred thousand")
        
    def test_1000000(self):
        self.assertEqual(self.instance.spellInteger("1000000"), "one million")
        
    def test_10000000(self):
        self.assertEqual(self.instance.spellInteger("10000000"), "ten million")
        
    def test_1234567(self):
        self.assertEqual(self.instance.spellInteger("1234567"), "one million two hundred thirty-four thousand five hundred sixty-seven")
        
    def test_4000000000(self):
        self.assertEqual(self.instance.spellInteger("4000000000"), "four billion")
        
    def test_999999999999(self):
        self.assertEqual(self.instance.spellInteger("999999999999"), "nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine")
        
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            self.instance.spellInteger("")
        
    def test_None(self):
        with self.assertRaises(TypeError):
            self.instance.spellInteger(None)
        
    def test_leading_zeroes(self):
        self.assertEqual(self.instance.spellInteger("0076"), "seventy-six")
        
    def test_all_zeroes(self):
        self.assertEqual(self.instance.spellInteger("00000"), "zero")
        
    
            
            
if __name__ == "__main__":
    unittest.main()