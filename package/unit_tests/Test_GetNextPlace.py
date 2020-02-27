import unittest
from ..integerSpeller import integerSpeller


class Test_GetNextPlace(unittest.TestCase):

    instance = integerSpeller()
    
    def test_zero(self):
        self.assertEqual(self.instance.getNextPlace(0), "")
        
    def test_two(self):
        self.assertEqual(self.instance.getNextPlace(2), "")
        
    def test_three(self):
        self.assertEqual(self.instance.getNextPlace(3), "thousand")
        
    def test_five(self):
        self.assertEqual(self.instance.getNextPlace(5), "thousand")
        
    def test_six(self):
        self.assertEqual(self.instance.getNextPlace(6), "million")
        
    def test_seven(self):
        self.assertEqual(self.instance.getNextPlace(7), "million")
        
    def test_nine(self):
        self.assertEqual(self.instance.getNextPlace(9), "billion")
        
        
if __name__ == "__main__":
    unittest.main()