def get_next_place(num_length):
    if 2 >= num_length >= 0:
        return ""

    elif 3 <= num_length <= 5:
        return "thousand"

    elif 6 <= num_length <= 8:
        return "million"

    elif 9 <= num_length <= 11:
        return "billion"

    else:
        raise ValueError("Out of Bounds: expected range [0, 12] but got " +
                         str(num_length))

# TODO: Make Unit Test for this function
def get_clean_int_string(num_str):
    # Resolve string of zeroes

    if set(num_str) == {"0"}:
        return "0"

    # Trim leading zeroes

    else:
        return num_str.lstrip("0")


class IntegerSpeller:

    """
    This class is meant to spell out positive integers
    """

    MAX_VALUE = 999999999999
    
    SINGLE_DIGIT_MAP = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    
    TEEN_MAP = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    
    DOUBLE_DIGIT_MAP = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    def __init__(self):
        pass

    def spell_one_digit(self, n):
    
        if type(n) != int:
            raise TypeError("Incorrect type: Expected int but got " + 
                str(type(n)))
            
        if n > 9 or n < 0:
            raise ValueError("Out of bounds: " + str(n) + " is not a " +
                             "single-digit, positive integer")
        
        return "zero" if n == 0 else self.SINGLE_DIGIT_MAP[n]

    def spell_two_digits(self, n):
    
        if type(n) != int:
            raise TypeError("Incorrect type: Expected int but got " + 
                str(type(n)))
            
        if n > 99 or n < 0:
            raise ValueError("Out of bounds: " + str(n) + " does not fall " +
                             "within range [0, 99] (inclusive)")
                
        if n < 10:
            return self.spell_one_digit(n)
            
        elif 10 <= n < 20:
            return self.TEEN_MAP[n]
            
        else:
            ones_place = n % 10
            tens_place = n - ones_place

            ones_place_string = ("-" + self.spell_one_digit(ones_place) if
                                 ones_place in self.SINGLE_DIGIT_MAP else "")

            return self.DOUBLE_DIGIT_MAP[tens_place] + ones_place_string

    def spell_three_digits(self, n):

        if type(n) != int:
            raise TypeError("Incorrect type: Expected int but got " +
                            str(type(n)))

        if n > 999 or n < 0:
            raise ValueError("Out of bounds: " + str(n) + " does not fall " +
                             "within range [0, 999] (inclusive)")

        if n < 100:
            return self.spell_two_digits(n)

        else:
            last_two_digits = n % 100
            hundreds_place_digit = int((n - last_two_digits) / 100)

            last_two_digits_str = self.spell_two_digits(last_two_digits)

            last_two_digits_str = (" " + last_two_digits_str if
                                   last_two_digits_str != "zero" else "")

            full_string = (self.spell_one_digit(hundreds_place_digit) +
                           " hundred" + last_two_digits_str)

            return full_string

    def spell_integer(self, n_str):

        def recurse(curr_str, len_after):

            # print(f"recurse: curr_str = {curr_str}, len_after = {len_after}")

            # TODO: Investigate if there is redundant handling of "000"

            if not curr_str or curr_str == "000":
                return ""

            curr_3 = curr_str[-3:]  # The current group of 3 digits
            curr_rest = curr_str[:-3]  # The remaining string of numbers

            place = get_next_place(len_after) if curr_3 != "000" else ""

            if len(curr_str) <= 3:
                three_digits_spelled = self.spell_three_digits(int(curr_str)) + " " + place
                return three_digits_spelled.rstrip()

            return_str = (recurse(curr_rest, len_after + 3) + " " +
                          recurse(curr_3, 0) + " " + place).rstrip()

            return return_str

        if type(n_str) != str:
            raise TypeError("Incorrect type: Expected int but got " +
                            str(type(n_str)))

        if not n_str.isdigit():
            raise ValueError("Expected numeric values in input but got non-" +
                             "numeric values")

        if int(n_str) > self.MAX_VALUE:
            raise ValueError("Out of bounds: input is greater than " +
                             str(self.MAX_VALUE))

        return recurse(get_clean_int_string(n_str), 0)


