from .IntegerSpeller import IntegerSpeller
import re


class NumberSpeller:
    """
    This class is meant to provide methods to spell out full numbers,
    regardless of whether they are integers, decimals, or negative
    """

    DECIMAL_PLACES_MAP = {
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

    MAX_DECIMAL_PLACES = max(DECIMAL_PLACES_MAP.keys())

    INTEGER_SPELLER = IntegerSpeller()

    def __init__(self):
        pass

    def spell_number(self, n_str):

        if type(n_str) != str:
            raise TypeError('Expected string but got ' + str(type(n_str)))

        int_regex = re.compile(r'^\d+$')
        decimal_regex = re.compile(r'^\d+?\.\d+$')
        neg_int_regex = re.compile(r'^\-\d+$')
        neg_decimal_regex = re.compile(r'^\-\d+?\.\d+$')

        if int_regex.match(n_str):
            return self.INTEGER_SPELLER.spell_integer(n_str)

        elif decimal_regex.match(n_str):
            num1, num2 = n_str.split('.')
            return self.INTEGER_SPELLER.spell_integer(num1) + ' and ' + self.spell_decimal(num2)

        elif neg_int_regex.match(n_str) or neg_decimal_regex.match(n_str):
            return 'negative ' + self.spell_number(n_str[1:])

        else:
            raise ValueError("Unrecognized input: " + n_str + "is not a number")

    def spell_decimal(self, n_str):  # FIXME: can this be a static method?
        """
        This method should only receive integer values in string format
        """

        if type(n_str) != str:
            raise TypeError('Expected string but got ' + str(type(n_str)))

        if not n_str.isdigit():
            raise ValueError('Expected numeric string but got ' + n_str)

        cleaned_n_str = n_str.rstrip('0')

        length = len(cleaned_n_str)

        if length > self.MAX_DECIMAL_PLACES:
            raise ValueError('Out of Bounds: Can handle up to ' +
                             str(self.MAX_DECIMAL_PLACES) + ' digits after the decimal but got ' +
                             str(length))

        spelled_int = self.INTEGER_SPELLER.spell_integer(cleaned_n_str)

        final_string = (spelled_int + ' ' + self.DECIMAL_PLACES_MAP[length])

        if spelled_int != 'one':
            final_string += 's'

        return final_string
