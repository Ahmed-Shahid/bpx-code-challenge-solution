

class integerSpeller:
    
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
      
      
    def spellOneDigit(self, n):
    
        if type(n) != int:
            raise TypeError("Incorrect type: Expected int but got " + 
                str(type(n)))
            
        if n > 9 or n < 0:
            raise ValueError("Out of bounds: " + str(n) + " is not a " +
                "single-digit, positive integer")
        
        return "zero" if n == 0 else self.SINGLE_DIGIT_MAP[n]
        
        
    def spellTwoDigits(self, n):
    
        if type(n) != int:
            raise TypeError("Incorrect type: Expected int but got " + 
                str(type(n)))
            
        if n > 99 or n < 0:
            raise ValueError("Out of bounds: " + str(n) + " does not fall " +
                "within range [0, 99] (inclusive)")
                
        if n < 10:
            return self.spellOneDigit(n)
            
        elif n >= 10 and n < 20:
            return self.TEEN_MAP[n]
            
        else:
            ones_place = n%10
            tens_place = n - ones_place
            
            ones_place_string = ("-"+self.spellOneDigit(ones_place) if 
                ones_place in self.SINGLE_DIGIT_MAP else "")
                
            return self.DOUBLE_DIGIT_MAP[tens_place] + ones_place_string
            
        
    def spellThreeDigits(self, n):
        
        if type(n) != int:
            raise TypeError("Incorrect type: Expected int but got " + type(n))
            
        if n > 999 or n < 0:
            raise ValueError("Out of bounds: " + str(n) + " does not fall " +
                "within range [0, 999] (inclusive)")
                
        if n < 100:
            return self.spellTwoDigits(n)
            
        else:
            last_two_digits = n%100
            hundreds_place_digit = int((n - last_two_digits)/100)
            
            last_two_digits_str = self.spellTwoDigits(last_two_digits)
            
            last_two_digits_str = (" "+last_two_digits_str if 
                last_two_digits_str != "zero" else "")
                
            full_string = (self.spellOneDigit(hundreds_place_digit) + 
                " hundred" + last_two_digits_str)
                
            return full_string
            
            