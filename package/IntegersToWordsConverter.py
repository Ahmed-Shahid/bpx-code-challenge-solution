

# ---------------------------- STATIC FUNCTIONS ---------------------------- #
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
        raise ValueError("Out of Bounds: expected range [0, 12] but got " + str(num_length))


# TODO: Make Unit Test for this function
def get_clean_int_string(num_str):

    # Resolve string of zeroes
    if set(num_str) == {"0"}:
        return "0"

    # Trim leading zeroes
    else:
        return num_str.lstrip("0")
# -------------------------------------------------------------------------- #


class IntegersToWordsConverter:
    """
    Converts only positive integers to words.  Input should be purely numeric strings.
    """
    def __init__(self):
        self.MAX_VALUE = 999999999999

        # Foundation for all greater numbers
        self.SINGLE_DIGIT_MAP = {
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

        # Adding this in because the teens are weird and rebellious
        self.TEEN_MAP = {
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
    
        self.DOUBLE_DIGIT_MAP = {
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety"
        }

    def convert_one_digit_to_word(self, n):
        """
        Input should be integer format in range 0-9
        """
    
        if type(n) != int:
            raise TypeError("Incorrect type: Expected int but got " + str(type(n)))
            
        if n > 9 or n < 0:
            raise ValueError("Out of bounds: " + str(n) + " is not a single-digit, positive integer")
        
        return "zero" if n == 0 else self.SINGLE_DIGIT_MAP[n]

    def convert_two_digits_to_word(self, n):
        """
        Input should be integer format in range 0-99
        """

        if type(n) != int:
            raise TypeError("Incorrect type: Expected int but got " + str(type(n)))
            
        if n < 0:
            raise ValueError("Out of bounds: Negative integer (" + str(n) + ") passed as input")
                
        elif 0 <= n < 10:
            return self.convert_one_digit_to_word(n)
            
        elif 10 <= n < 20:
            return self.TEEN_MAP[n]
            
        elif 20 <= n < 100:
            ones_place = n % 10
            tens_place = n - ones_place

            ones_place_string = ("-" + self.convert_one_digit_to_word(ones_place) if
                                 ones_place in self.SINGLE_DIGIT_MAP else "")

            return self.DOUBLE_DIGIT_MAP[tens_place] + ones_place_string

        elif n >= 100:
            raise ValueError("Out of bounds: Input (" + str(n) + ") is greater than 99")

    def convert_three_digits_to_word(self, n):
        """
        Input should be integer format in range 0-99
        """

        if type(n) != int:
            raise TypeError("Incorrect type: Expected int but got " + str(type(n)))

        if n < 0:
            raise ValueError("Out of bounds: Negative integer (" + str(n) + ") passed as input")

        elif 0 <= n < 100:
            return self.convert_two_digits_to_word(n)

        elif 100 <= n < 1000:
            last_two_digits = n % 100
            hundreds_place_digit = int((n - last_two_digits) / 100)

            last_two_digits_str = self.convert_two_digits_to_word(last_two_digits)

            last_two_digits_str = (" " + last_two_digits_str if
                                   last_two_digits_str != "zero" else "")

            full_string = (self.convert_one_digit_to_word(hundreds_place_digit) +
                           " hundred" + last_two_digits_str)

            return full_string

        elif n >= 1000:
            raise ValueError("Out of bounds: Input (" + str(n) + ") is greater than 999")

    def convert_integer_to_word(self, n_str):
        """
        Input may be any positive integer less than MAX_VALUE.
        """

        # Nested function for recursion
        # This function will start with the full integer string and cut off digits from the
        # right in groups of three
        def recurse(curr_str, len_after):

            # End condition and also a "skip" for a group of 3 zeroes caught in the middle
            # (i.e. 1,245,000,783)
            #             ^^^
            if not curr_str or curr_str == "000":
                return ""

            curr_3 = curr_str[-3:]  # The current group of 3 digits
            curr_rest = curr_str[:-3]  # The remaining string of numbers

            # "Place" text (i.e. thousand, million, etc)
            # this is also blank if the current group of 3 digits is "000"
            place = get_next_place(len_after) if curr_3 != "000" else ""

            # Another end condition (i.e. the last group of 1, 2, or 3 digits)
            if len(curr_str) <= 3:
                final_digits_as_word = self.convert_three_digits_to_word(int(curr_str)) + " " + place
                return final_digits_as_word.rstrip()

            # Essentially: Get the rest + Get the current group of 3 + thousand/million/etc.
            # Also, trim trailing spaces
            return_str = (recurse(curr_rest, len_after + 3) + " " + recurse(curr_3, 0) + " " + place).rstrip()

            return return_str

        # "Main" block of this function
        if type(n_str) != str:
            raise TypeError("Incorrect type: Expected int but got " + str(type(n_str)))

        if not n_str.isdigit():
            raise ValueError("Incorrect value: " + n_str + "is not a numeric input")

        if int(n_str) > self.MAX_VALUE:
            raise ValueError("Out of bounds: input is greater than " + str(self.MAX_VALUE))

        return recurse(get_clean_int_string(n_str), 0)


