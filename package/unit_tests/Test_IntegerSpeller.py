import unittest
from package.IntegerSpeller import IntegerSpeller, get_next_place


class Test_SpellInteger(unittest.TestCase):

    instance = IntegerSpeller()
    
    def test_zero(self):
        self.assertEqual(self.instance.spell_integer("0"), "zero")
        
    def test_four(self):
        self.assertEqual(self.instance.spell_integer("4"), "four")
        
    def test_nine(self):
        self.assertEqual(self.instance.spell_integer("9"), "nine")
        
    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.spell_integer("-1")
            
        with self.assertRaises(ValueError):
            self.instance.spell_integer("1000000000000")
            
        with self.assertRaises(ValueError):
            self.instance.spell_integer("4351534354879")
            
    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
        # self.assertEqual(self.instance.spellInteger(01), "one")
        
    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.spell_integer(23)
            
        with self.assertRaises(TypeError):
            self.instance.spell_integer(774.0)
            
        with self.assertRaises(TypeError):
            self.instance.spell_integer(3675.5)
            
    def test_ten(self):
        self.assertEqual(self.instance.spell_integer("10"), "ten")
        
    def test_sixteen(self):
        self.assertEqual(self.instance.spell_integer("16"), "sixteen")
        
    def test_twenty(self):
        self.assertEqual(self.instance.spell_integer("20"), "twenty")
        
    def test_thirty_two(self):
        self.assertEqual(self.instance.spell_integer("32"), "thirty-two")
        
    def test_eighty_eight(self):
        self.assertEqual(self.instance.spell_integer("88"), "eighty-eight")
        
    def test_two_thirty_six(self):
        self.assertEqual(self.instance.spell_integer("236"), "two hundred thirty-six")
        
    def test_nine_ninety_nine(self):
        self.assertEqual(self.instance.spell_integer("999"), "nine hundred ninety-nine")
        
    def test_six_hundred(self):
        self.assertEqual(self.instance.spell_integer("600"), "six hundred")
        
    def test_2535(self):
        self.assertEqual(self.instance.spell_integer("2535"), "two thousand five hundred thirty-five")
        
    def test_1000(self):
        self.assertEqual(self.instance.spell_integer("1000"), "one thousand")
        
    def test_5076(self):
        self.assertEqual(self.instance.spell_integer("5076"), "five thousand seventy-six")
        
    def test_111111(self):
        self.assertEqual(self.instance.spell_integer("111111"), "one hundred eleven thousand one hundred eleven")
        
    def test_100000(self):
        self.assertEqual(self.instance.spell_integer("100000"), "one hundred thousand")
        
    def test_1000000(self):
        self.assertEqual(self.instance.spell_integer("1000000"), "one million")
        
    def test_10000000(self):
        self.assertEqual(self.instance.spell_integer("10000000"), "ten million")
        
    def test_1234567(self):
        self.assertEqual(self.instance.spell_integer("1234567"), "one million two hundred thirty-four thousand five hundred sixty-seven")
        
    def test_4000000000(self):
        self.assertEqual(self.instance.spell_integer("4000000000"), "four billion")
        
    def test_999999999999(self):
        self.assertEqual(self.instance.spell_integer("999999999999"), "nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine")
        
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            self.instance.spell_integer("")
        
    def test_None(self):
        with self.assertRaises(TypeError):
            self.instance.spell_integer(None)
        
    def test_leading_zeroes(self):
        self.assertEqual(self.instance.spell_integer("0076"), "seventy-six")
        
    def test_all_zeroes(self):
        self.assertEqual(self.instance.spell_integer("00000"), "zero")


class Test_GetNextPlace(unittest.TestCase):
    instance = IntegerSpeller()

    def test_zero(self):
        self.assertEqual(get_next_place(0), "")

    def test_two(self):
        self.assertEqual(get_next_place(2), "")

    def test_three(self):
        self.assertEqual(get_next_place(3), "thousand")

    def test_five(self):
        self.assertEqual(get_next_place(5), "thousand")

    def test_six(self):
        self.assertEqual(get_next_place(6), "million")

    def test_seven(self):
        self.assertEqual(get_next_place(7), "million")

    def test_nine(self):
        self.assertEqual(get_next_place(9), "billion")


class Test_SpellOneDigit(unittest.TestCase):
    instance = IntegerSpeller()

    def test_zero(self):
        self.assertEqual(self.instance.spell_one_digit(0), "zero")

    def test_four(self):
        self.assertEqual(self.instance.spell_one_digit(4), "four")

    def test_nine(self):
        self.assertEqual(self.instance.spell_one_digit(9), "nine")

    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.spell_one_digit(-1)

        with self.assertRaises(ValueError):
            self.instance.spell_one_digit(10)

        with self.assertRaises(ValueError):
            self.instance.spell_one_digit(55)

    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
    # self.assertEqual(self.instance.spellOneDigit(01), "one")

    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.spell_one_digit("2")

        with self.assertRaises(TypeError):
            self.instance.spell_one_digit(7.0)

        with self.assertRaises(TypeError):
            self.instance.spell_one_digit(5.5)


class Test_SpellTwoDigits(unittest.TestCase):
    instance = IntegerSpeller()

    def test_zero(self):
        self.assertEqual(self.instance.spell_two_digits(0), "zero")

    def test_four(self):
        self.assertEqual(self.instance.spell_two_digits(4), "four")

    def test_nine(self):
        self.assertEqual(self.instance.spell_two_digits(9), "nine")

    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.spell_two_digits(-1)

        with self.assertRaises(ValueError):
            self.instance.spell_two_digits(100)

        with self.assertRaises(ValueError):
            self.instance.spell_two_digits(450)

    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
    # self.assertEqual(self.instance.spellTwoDigits(01), "one")

    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.spell_two_digits("23")

        with self.assertRaises(TypeError):
            self.instance.spell_two_digits(77.0)

        with self.assertRaises(TypeError):
            self.instance.spell_two_digits(35.5)

    def test_ten(self):
        self.assertEqual(self.instance.spell_two_digits(10), "ten")

    def test_sixteen(self):
        self.assertEqual(self.instance.spell_two_digits(16), "sixteen")

    def test_twenty(self):
        self.assertEqual(self.instance.spell_two_digits(20), "twenty")

    def test_thirty_two(self):
        self.assertEqual(self.instance.spell_two_digits(32), "thirty-two")

    def test_eighty_eight(self):
        self.assertEqual(self.instance.spell_two_digits(88), "eighty-eight")


class Test_SpellThreeDigits(unittest.TestCase):
    instance = IntegerSpeller()

    def test_zero(self):
        self.assertEqual(self.instance.spell_three_digits(0), "zero")

    def test_four(self):
        self.assertEqual(self.instance.spell_three_digits(4), "four")

    def test_nine(self):
        self.assertEqual(self.instance.spell_three_digits(9), "nine")

    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.spell_three_digits(-1)

        with self.assertRaises(ValueError):
            self.instance.spell_three_digits(1000)

        with self.assertRaises(ValueError):
            self.instance.spell_three_digits(435153)

    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
    # self.assertEqual(self.instance.spellThreeDigits(01), "one")

    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.spell_three_digits("23")

        with self.assertRaises(TypeError):
            self.instance.spell_three_digits(77.0)

        with self.assertRaises(TypeError):
            self.instance.spell_three_digits(35.5)

    def test_ten(self):
        self.assertEqual(self.instance.spell_three_digits(10), "ten")

    def test_sixteen(self):
        self.assertEqual(self.instance.spell_three_digits(16), "sixteen")

    def test_twenty(self):
        self.assertEqual(self.instance.spell_three_digits(20), "twenty")

    def test_thirty_two(self):
        self.assertEqual(self.instance.spell_three_digits(32), "thirty-two")

    def test_eighty_eight(self):
        self.assertEqual(self.instance.spell_three_digits(88), "eighty-eight")

    def test_two_thirty_six(self):
        self.assertEqual(self.instance.spell_three_digits(236), "two hundred thirty-six")

    def test_nine_ninety_nine(self):
        self.assertEqual(self.instance.spell_three_digits(999), "nine hundred ninety-nine")

    def test_six_hundred(self):
        self.assertEqual(self.instance.spell_three_digits(600), "six hundred")


if __name__ == "__main__":
    unittest.main()
