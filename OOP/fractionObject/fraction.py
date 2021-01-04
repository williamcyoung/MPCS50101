class Fraction:
    # initialize numerator, denominator; raise exception if denominator is zero
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ZeroDivisionError
        self.as_decimal = float(self.as_decimal())
    
    # need to find lcd to add
    def _lcd(self, other_fraction):
        return int((self.denominator * other_fraction.denominator) /  _gcd(self.denominator, other_fraction.denominator))

    def __add__(self, other_fraction):
        # get lcd. This will be the denominator of the sum of the two fractions if we cannot simplify
        lcd = self._lcd(other_fraction)
        # with lcd in the denominator, we add the two numerators
        numerator_sum = int((self.numerator * (lcd / self.denominator)) + (other_fraction.numerator * (lcd / other_fraction.denominator)))
        
        # get gcd to simplify
        gcd = _gcd(numerator_sum, lcd)

        return Fraction(int(numerator_sum/gcd), int(lcd/gcd))

    # subtracting is similar
    def __sub__(self, other_fraction):
        
        lcd = self._lcd(other_fraction)
        
        numerator_diff = int((self.numerator * (lcd / self.denominator)) - (other_fraction.numerator * (lcd / other_fraction.denominator)))
        
        # get gcd to simplify
        gcd = _gcd(numerator_diff, lcd)

        return Fraction(int(numerator_diff/gcd), int(lcd/gcd))

    # multiplying is straightforward, but need to get gcd to simplify
    def __mul__(self, other_fraction):
        
        mul_numerator = (self.numerator * other_fraction.numerator)
        
        mul_denominator = (self.denominator * other_fraction.denominator)
        
        gcd = _gcd(mul_numerator, mul_denominator)
        
        return Fraction(int((mul_numerator)/gcd), int((mul_denominator)/gcd))

    # dividing is just multiplying by the reciprocal
    def __truediv__(self, other_fraction):
        
        div_numerator = (self.numerator * other_fraction.denominator)
        
        div_denominator = (self.denominator * other_fraction.numerator)
        
        gcd = _gcd(div_numerator, div_denominator)
        
        return Fraction(int((div_numerator)/gcd), int((div_denominator)/gcd))

    # comparators; just check if one fraction is greater than / less than the other
    def __gt__(self, other_fraction):
        if (self.numerator / self.denominator) > (other_fraction.numerator / other_fraction.denominator):
            return True
        else:
            return False

    def __lt__(self, other_fraction):
        if (self.numerator / self.denominator) < (other_fraction.numerator / other_fraction.denominator):
            return True
        else:
            return False
    
    # method to get fraction as decimal string, formatted to 3 decimal places
    def as_decimal(self):
        decimal = self.numerator/self.denominator
        return "%.3f" % decimal

    def __str__(self):
        if self.numerator == 0:
            return "0"
        elif self.numerator < self.denominator:
            return "%s/%s" % (self.numerator, self.denominator)
        elif self.numerator > self.denominator:
            if self.numerator%self.denominator == 0:
                return "%s" % (self.numerator // self.denominator)
            else:
                return "%s-%s/%s" % (self.numerator // self.denominator, (self.numerator)%(self.denominator), self.denominator)
        else:
            return "%s" % (self.numerator // self.denominator)

def _gcd(a, b):
        # get the remainder
        r = (a % b)
        # if the remainder is zero, the algorithm breaks (base case)
        if r == 0:
            return b
        # otherwise, gcd(a, b) = gcd(b, r)
        else:
            return _gcd(b, r)