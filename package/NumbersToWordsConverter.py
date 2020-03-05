from .IntegersToWordsConverter import IntegersToWordsConverter
import re


class NumbersToWordsConverter:
    """
    Provides methods to convert full numbers to word representation,
    regardless of whether numbers are integers, decimals, or negative
    """

    def __init__(self):
        self.DECIMAL_PLACES_MAP = {
            1: "tenth",
            2: "hundredth",
            3: "thousandth",
            4: "ten-thousandth",
            5: "hundred-thousandth",
            6: "millionth",
            7: "ten-millionth",
            8: "hundred-millionth",
            9: "billionth",
            10: "ten-billionth",
            11: "hundred-billionth",
        }
        self.MAX_DECIMAL_PLACES = max(self.DECIMAL_PLACES_MAP.keys())
        self.INTEGER_CONVERTER = IntegersToWordsConverter()

    def convert_number_to_word(self, n_str):
        """
        Method converts integers, decimals, and negative numbers
        """

        if type(n_str) != str:
            raise TypeError('Expected string but got ' + str(type(n_str)))

        # Possible input formats to cycle through (in regex)
        int_regex = re.compile(r'^\d+$')
        decimal_regex = re.compile(r'^\d+?\.\d+$')
        neg_int_regex = re.compile(r'^\-\d+$')
        neg_decimal_regex = re.compile(r'^\-\d+?\.\d+$')

        # Positive Integer
        if int_regex.match(n_str):
            return self.INTEGER_CONVERTER.convert_integer_to_word(n_str)

        # Positive Decimal
        # Replace decimal point with 'and'
        elif decimal_regex.match(n_str):
            num1, num2 = n_str.split('.')
            return self.INTEGER_CONVERTER.convert_integer_to_word(num1) + ' and ' + self.convert_decimal_to_word(num2)

        # Negative Integer or Decimal
        # Same as a positive num with 'negative' prepended
        elif neg_int_regex.match(n_str) or neg_decimal_regex.match(n_str):
            return 'negative ' + self.convert_number_to_word(n_str[1:])

        else:
            raise ValueError("Unrecognized input: " + n_str + " is not a number")

    def convert_decimal_to_word(self, n_str):  # FIXME: can this be a static method?
        """
        This method should only receive integer values in string format
        """

        if type(n_str) != str:
            raise TypeError('Expected string but got ' + str(type(n_str)))

        if not n_str.isdigit():
            raise ValueError('Expected numeric string but got ' + n_str)

        # Remove trailing zeroes
        cleaned_n_str = n_str.rstrip('0')

        length = len(cleaned_n_str)

        if length > self.MAX_DECIMAL_PLACES:
            raise ValueError('Out of Bounds: Can handle up to ' +
                             str(self.MAX_DECIMAL_PLACES) +
                             ' digits after the decimal but got ' +
                             str(length))

        # Basic functionality is to return integer word appended by 'decimal place' word

        int_word = self.INTEGER_CONVERTER.convert_integer_to_word(cleaned_n_str)

        final_string = (int_word + ' ' + self.DECIMAL_PLACES_MAP[length])

        if int_word != 'one':
            final_string += 's'  # Because... you know... plurals and stuff

        return final_string
