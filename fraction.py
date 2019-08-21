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

        # Raise an errors
        if numerator == 0 and denominator == 0:
            raise ValueError('0/0 are undefine value.')
        if (numerator in [math.inf, -math.inf]) and (denominator in [math.inf, -math.inf]):
            raise ValueError(f'{numerator}/{denominator} are undefine value.')
        if not isinstance(numerator, (int, float)):
            raise TypeError(f'{numerator} is neither real number nor infinity')
        elif not isinstance(denominator, (int, float)):
            raise TypeError(f'{denominator} is neither real number nor infinity')

        # Inittialize
        # self.numerator = numerator
        # self.denominator = denominator

        # Check Is the fraction an infinity? 
        # and Is the fraction a negative?
        if denominator == 0:
            self.is_infinity = True
            if numerator >= 0:
                self.is_negative = False
            else:
                self.is_negative = True

            # Set new value for infinity
            self.numerator = 1
            self.denominator = 0

        elif denominator in [math.inf, -math.inf]:
            # Set new value
            self.numerator = 0
            self.denominator = 1

            self.is_negative = False
            self.is_infinity = False

        elif numerator in [math.inf, -math.inf]:
            self.is_infinity = True
            if numerator / denominator > 0:
                self.is_negative = False
            else:
                self.is_negative = True

            # Set new value for infinity
            self.numerator = 1
            self.denominator = 0

        else:
            # init
            self.numerator = numerator
            self.denominator = denominator
            self.is_infinity = False

            if self.numerator / self.denominator >= 0:
                self.is_negative = False
            else:
                self.is_negative = True

        # round both parameter, (not nessary if both parameter are integer)
        if not self.is_infinity:
            self.numerator = round(self.numerator)
            self.denominator = round(self.denominator)

        if self.numerator != 0 or self.denominator != 0:
            # Find GCD of this fraction
            self.gcd = math.gcd(abs(self.numerator), abs(self.denominator))

            # change fraction to proper fracion
            self.numerator = int(self.numerator / self.gcd)
            self.denominator = int(self.denominator / self.gcd)

        # set the negative sign (it will appear in front of numerator)
        if self.is_negative:
            self.numerator = -abs(self.numerator)
            self.denominator = abs(self.denominator)
        else:
            self.numerator = abs(self.numerator)
            self.denominator = abs(self.denominator)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        if self.__str__() == 'inf':
            if frac.__str__() == '-inf':
                raise ValueError(f'({self.__str__()}) + ({self.__str__()}) is undefine.')
            else:
                return Fraction(1, 0)
        elif self.__str__() == '-inf':
            if frac.__str__() == 'inf':
                raise ValueError(f'({self.__str__()}) + ({self.__str__()}) is undefine.')
            else:
                return Fraction(-1, 0)
        numerator = self.numerator * frac.denominator + frac.numerator * self.denominator
        denominator = self.denominator * frac.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, frac):
        if self.numerator * frac.numerator == 0 and self.denominator * frac.denominator == 0:
            if (self.__str__() in ['inf', '-inf']) and (frac.numerator == 0):
                return Fraction(0, 1)
            elif (frac.__str__() in ['inf', '-inf']) and (self.numerator == 0):
                return Fraction(0, 1)
        else:
            return Fraction(self.numerator * frac.numerator, self.denominator * frac.denominator)

    def __sub__(self, frac):
        if self.__str__() == 'inf':
            if frac.__str__() == '-inf':
                raise ValueError(f'({self.__str__()}) - ({self.__str__()}) is undefine.')
            else:
                return Fraction(1, 0)
        elif self.__str__() == '-inf':
            if frac.__str__() == 'inf':
                raise ValueError(f'({self.__str__()}) - ({self.__str__()}) is undefine.')
            else:
                return Fraction(-1, 0)
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
        elif self.denominator == 1:
            return f'{self.numerator}'
        else:
            return f'{self.numerator}/{self.denominator}'

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.__str__() == frac.__str__()