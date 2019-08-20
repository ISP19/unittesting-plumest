import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """

    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if numerator == 0 and denominator == 0:
            raise ValueError('0/0 are undefine value.')
        if (numerator in [math.inf, -math.inf]) and (denominator in [math.inf, -math.inf]):
            raise ValueError(f'{numerator}/{denominator} are undefine value.')
        if not isinstance(numerator, (int, float)):
            raise TypeError(f'{numerator} is neither real number nor infinity')
        elif not isinstance(denominator, (int, float)):
            raise TypeError(f'{denominator} is neither real number nor infinity')

        self.numerator = numerator
        self.denominator = denominator
        if -math.inf < self.numerator < math.inf:
            self.numerator = round(self.numerator)
            if -math.inf < self.denominator < math.inf:
                self.denominator = round(self.denominator)
                if self.numerator != 0 and self.denominator != 0:
                    self.gcd = math.gcd(abs(self.numerator), abs(self.denominator))

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = self.numerator * frac.denominator + frac.numerator * self.denominator
        denominator = self.denominator * frac.denominator
        return Fraction(numerator, denominator)

    # TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    # Optional have fun and overload other operators such as
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)
    def __mul__(self, frac):
        if self.numerator * frac.numerator == 0 and self.denominator * frac.denominator == 0:
            if (self.__str__() in ['inf', '-inf']) and (frac.__str__ in [0]):
                return Fraction(0, math.inf)
        else:
            return Fraction(self.numerator * frac.numerator, self.denominator * frac.denominator)

    def __sub__(self, frac):
        numerator = self.numerator * frac.denominator - frac.numerator * self.denominator
        denominator = self.denominator * frac.denominator
        return Fraction(numerator, denominator)

    def __gt__(self, frac):
        if (self.__str__() == 'inf') and (frac.__str__() == 'inf'):
            return False
        elif (self.__str__() == 'inf') and (int(frac.__str__()) < math.inf):
            return True
        elif int(self.__str__()) < int(frac.__str__()):
            return True
        else:
            return False

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __str__(self):
        if self.numerator == 0:
            return '0'
        elif self.denominator == 0 and self.numerator > 0:
            return f'{math.inf}'
        elif self.denominator == 0 and self.numerator < 0:
            return f'{-math.inf}'
        elif self.numerator == math.inf and self.denominator > 0:
            return f'{math.inf}'
        elif self.numerator == math.inf and self.denominator < 0:
            return f'{-math.inf}'
        elif self.numerator == -math.inf and self.denominator > 0:
            return f'{-math.inf}'
        elif self.numerator == -math.inf and self.denominator < 0:
            return f'{math.inf}'
        elif self.denominator == math.inf or self.denominator == -math.inf:
            return f'0'
        elif self.numerator % self.denominator == 0:
            return f'{int(self.numerator/self.denominator)}'
        elif self.numerator / self.denominator < 0:
            return f'-{int(self.numerator / self.gcd)}/{int(abs(self.denominator / self.gcd))}'
        else:
            return f'{int(abs(self.numerator / self.gcd))}/{int(abs(self.denominator / self.gcd))}'

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        if self.__str__() == frac.__str__():
            return True
        else:
            return False

a = Fraction(1, 0)
b = Fraction(-1, 0)
c = Fraction(0, 1)
d = Fraction(0, -1)
# e = Fraction(0, 0)
f = Fraction(1, 1)

print(a.__mul__(c))