import unittest
from package.NumbersToWordsConverter import NumbersToWordsConverter


class Test_SpellDecimal(unittest.TestCase):
    NUMSPELL = NumbersToWordsConverter()

    def test_point_1(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("1"), "one tenth")

    def test_point_6(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("6"), "six tenths")

    def test_point_01(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("01"), "one hundredth")

    def test_point_03(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("03"), "three hundredths")

    def test_point_47(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("47"), "forty-seven hundredths")

    def test_point_001(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("001"), "one thousandth")

    def test_point_201(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("201"), "two hundred one thousandths")

    def test_point_400(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("400"), "four tenths")

    def test_point_0001(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("0001"), "one ten-thousandth")

    def test_point_00001(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("00001"), "one hundred-thousandth")

    def test_point_000001(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("000001"), "one millionth")

    def test_point_0000001(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("0000001"), "one ten-millionth")

    def test_point_0000001(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("00000001"), "one hundred-millionth")

    def test_point_9999999999(self):
        self.assertEqual(self.NUMSPELL.convert_decimal_to_word("99999999999"), "ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine hundred-billionths")

    def test_out_of_bounds(self):
        with self.assertRaises(ValueError):
            self.NUMSPELL.convert_decimal_to_word("000000000001")

    def test_invalid_character(self):
        with self.assertRaises(ValueError):
            self.NUMSPELL.convert_decimal_to_word("-0000001")

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            self.NUMSPELL.convert_decimal_to_word(2)


class Test_SpellNumber(unittest.TestCase):
    NUMSPELL = NumbersToWordsConverter()

    def test_zero(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("0"), "zero")

    def test_four(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("4"), "four")

    def test_nine(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("9"), "nine")

    def test_ten(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("10"), "ten")

    def test_sixteen(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("16"), "sixteen")

    def test_twenty(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("20"), "twenty")

    def test_thirty_two(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("32"), "thirty-two")

    def test_eighty_eight(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("88"), "eighty-eight")

    def test_two_thirty_six(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("236"), "two hundred thirty-six")

    def test_nine_ninety_nine(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("999"), "nine hundred ninety-nine")

    def test_six_hundred(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("600"), "six hundred")

    def test_2535(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("2535"), "two thousand five hundred thirty-five")

    def test_1000(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("1000"), "one thousand")

    def test_5076(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("5076"), "five thousand seventy-six")

    def test_111111(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("111111"), "one hundred eleven thousand one hundred eleven")

    def test_100000(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("100000"), "one hundred thousand")

    def test_1000000(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("1000000"), "one million")

    def test_10000000(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("10000000"), "ten million")

    def test_1234567(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("1234567"),
                         "one million two hundred thirty-four thousand five hundred sixty-seven")

    def test_4000000000(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("4000000000"), "four billion")

    def test_999999999999(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("999999999999"),
                         "nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            self.NUMSPELL.convert_number_to_word("")

    def test_None(self):
        with self.assertRaises(TypeError):
            self.NUMSPELL.convert_number_to_word(None)

    def test_leading_zeroes(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("0076"), "seventy-six")

    def test_all_zeroes(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("00000"), "zero")

    def test_101_point_5(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("101.5"), 'one hundred one and five tenths')

    def test_0_point_45354(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("0.45354"), 'zero and forty-five thousand three hundred fifty-four hundred-thousandths')

    def test_999999_point_9955559(self):
        self.assertEqual(self.NUMSPELL.convert_number_to_word("999999.9955559"), 'nine hundred ninety-nine thousand nine hundred ninety-nine and nine million nine hundred fifty-five' +
                                                                       ' thousand five hundred fifty-nine ten-millionths')


if __name__ == '__main__':
    unittest.main()
