import unittest
from package.IntegersToWordsConverter import IntegersToWordsConverter, get_next_place


class TestConvertIntToWord(unittest.TestCase):

    instance = IntegersToWordsConverter()
    
    def test_zero(self):
        self.assertEqual(self.instance.convert_integer_to_word("0"), "zero")
        
    def test_four(self):
        self.assertEqual(self.instance.convert_integer_to_word("4"), "four")
        
    def test_nine(self):
        self.assertEqual(self.instance.convert_integer_to_word("9"), "nine")
        
    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.convert_integer_to_word("-1")
            
        with self.assertRaises(ValueError):
            self.instance.convert_integer_to_word("1000000000000")
            
        with self.assertRaises(ValueError):
            self.instance.convert_integer_to_word("4351534354879")
            
    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
        # self.assertEqual(self.instance.spellInteger(01), "one")
        
    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.convert_integer_to_word(23)
            
        with self.assertRaises(TypeError):
            self.instance.convert_integer_to_word(774.0)
            
        with self.assertRaises(TypeError):
            self.instance.convert_integer_to_word(3675.5)
            
    def test_ten(self):
        self.assertEqual(self.instance.convert_integer_to_word("10"), "ten")
        
    def test_sixteen(self):
        self.assertEqual(self.instance.convert_integer_to_word("16"), "sixteen")
        
    def test_twenty(self):
        self.assertEqual(self.instance.convert_integer_to_word("20"), "twenty")
        
    def test_thirty_two(self):
        self.assertEqual(self.instance.convert_integer_to_word("32"), "thirty-two")
        
    def test_eighty_eight(self):
        self.assertEqual(self.instance.convert_integer_to_word("88"), "eighty-eight")
        
    def test_two_thirty_six(self):
        self.assertEqual(self.instance.convert_integer_to_word("236"), "two hundred thirty-six")
        
    def test_nine_ninety_nine(self):
        self.assertEqual(self.instance.convert_integer_to_word("999"), "nine hundred ninety-nine")
        
    def test_six_hundred(self):
        self.assertEqual(self.instance.convert_integer_to_word("600"), "six hundred")
        
    def test_2535(self):
        self.assertEqual(self.instance.convert_integer_to_word("2535"), "two thousand five hundred thirty-five")
        
    def test_1000(self):
        self.assertEqual(self.instance.convert_integer_to_word("1000"), "one thousand")
        
    def test_5076(self):
        self.assertEqual(self.instance.convert_integer_to_word("5076"), "five thousand seventy-six")
        
    def test_111111(self):
        self.assertEqual(self.instance.convert_integer_to_word("111111"), "one hundred eleven thousand one hundred eleven")
        
    def test_100000(self):
        self.assertEqual(self.instance.convert_integer_to_word("100000"), "one hundred thousand")
        
    def test_1000000(self):
        self.assertEqual(self.instance.convert_integer_to_word("1000000"), "one million")
        
    def test_10000000(self):
        self.assertEqual(self.instance.convert_integer_to_word("10000000"), "ten million")
        
    def test_1234567(self):
        self.assertEqual(self.instance.convert_integer_to_word("1234567"), "one million two hundred thirty-four thousand five hundred sixty-seven")
        
    def test_4000000000(self):
        self.assertEqual(self.instance.convert_integer_to_word("4000000000"), "four billion")
        
    def test_999999999999(self):
        self.assertEqual(self.instance.convert_integer_to_word("999999999999"), "nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine")
        
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            self.instance.convert_integer_to_word("")
        
    def test_None(self):
        with self.assertRaises(TypeError):
            self.instance.convert_integer_to_word(None)
        
    def test_leading_zeroes(self):
        self.assertEqual(self.instance.convert_integer_to_word("0076"), "seventy-six")
        
    def test_all_zeroes(self):
        self.assertEqual(self.instance.convert_integer_to_word("00000"), "zero")


class TestGetNextPlace(unittest.TestCase):
    instance = IntegersToWordsConverter()

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


class TestConvertOneDigitToWord(unittest.TestCase):
    instance = IntegersToWordsConverter()

    def test_zero(self):
        self.assertEqual(self.instance.convert_one_digit_to_word(0), "zero")

    def test_four(self):
        self.assertEqual(self.instance.convert_one_digit_to_word(4), "four")

    def test_nine(self):
        self.assertEqual(self.instance.convert_one_digit_to_word(9), "nine")

    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.convert_one_digit_to_word(-1)

        with self.assertRaises(ValueError):
            self.instance.convert_one_digit_to_word(10)

        with self.assertRaises(ValueError):
            self.instance.convert_one_digit_to_word(55)

    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
    # self.assertEqual(self.instance.spellOneDigit(01), "one")

    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.convert_one_digit_to_word("2")

        with self.assertRaises(TypeError):
            self.instance.convert_one_digit_to_word(7.0)

        with self.assertRaises(TypeError):
            self.instance.convert_one_digit_to_word(5.5)


class TestConvertTwoDigitsToWord(unittest.TestCase):
    instance = IntegersToWordsConverter()

    def test_zero(self):
        self.assertEqual(self.instance.convert_two_digits_to_word(0), "zero")

    def test_four(self):
        self.assertEqual(self.instance.convert_two_digits_to_word(4), "four")

    def test_nine(self):
        self.assertEqual(self.instance.convert_two_digits_to_word(9), "nine")

    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.convert_two_digits_to_word(-1)

        with self.assertRaises(ValueError):
            self.instance.convert_two_digits_to_word(100)

        with self.assertRaises(ValueError):
            self.instance.convert_two_digits_to_word(450)

    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
    # self.assertEqual(self.instance.spellTwoDigits(01), "one")

    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.convert_two_digits_to_word("23")

        with self.assertRaises(TypeError):
            self.instance.convert_two_digits_to_word(77.0)

        with self.assertRaises(TypeError):
            self.instance.convert_two_digits_to_word(35.5)

    def test_ten(self):
        self.assertEqual(self.instance.convert_two_digits_to_word(10), "ten")

    def test_sixteen(self):
        self.assertEqual(self.instance.convert_two_digits_to_word(16), "sixteen")

    def test_twenty(self):
        self.assertEqual(self.instance.convert_two_digits_to_word(20), "twenty")

    def test_thirty_two(self):
        self.assertEqual(self.instance.convert_two_digits_to_word(32), "thirty-two")

    def test_eighty_eight(self):
        self.assertEqual(self.instance.convert_two_digits_to_word(88), "eighty-eight")


class TestConvertThreeDigitsToWord(unittest.TestCase):
    instance = IntegersToWordsConverter()

    def test_zero(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(0), "zero")

    def test_four(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(4), "four")

    def test_nine(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(9), "nine")

    def test_outOfBounds(self):
        with self.assertRaises(ValueError):
            self.instance.convert_three_digits_to_word(-1)

        with self.assertRaises(ValueError):
            self.instance.convert_three_digits_to_word(1000)

        with self.assertRaises(ValueError):
            self.instance.convert_three_digits_to_word(435153)

    # Cannot define an integer with leading zeroes
    # def test_notOutOfBounds(self):
    # self.assertEqual(self.instance.spellThreeDigits(01), "one")

    def test_wrongType(self):
        with self.assertRaises(TypeError):
            self.instance.convert_three_digits_to_word("23")

        with self.assertRaises(TypeError):
            self.instance.convert_three_digits_to_word(77.0)

        with self.assertRaises(TypeError):
            self.instance.convert_three_digits_to_word(35.5)

    def test_ten(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(10), "ten")

    def test_sixteen(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(16), "sixteen")

    def test_twenty(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(20), "twenty")

    def test_thirty_two(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(32), "thirty-two")

    def test_eighty_eight(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(88), "eighty-eight")

    def test_two_thirty_six(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(236), "two hundred thirty-six")

    def test_nine_ninety_nine(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(999), "nine hundred ninety-nine")

    def test_six_hundred(self):
        self.assertEqual(self.instance.convert_three_digits_to_word(600), "six hundred")


if __name__ == "__main__":
    unittest.main()
