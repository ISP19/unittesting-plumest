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
        if not isinstance(numerator, (int, float)):
            raise TypeError(f'{numerator} is neither real number nor infinity')
        elif not isinstance(denominator, (int, float)):
            raise TypeError(f'{denominator} is neither real number nor infinity')

        # Check Is the fraction an infinity? 
        # Check Is the fraction an 0/0 (nan)? 
        # and Is the fraction a negative?
        if (numerator in [math.inf, -math.inf]) and (denominator in [math.inf, -math.inf]):
            self.is_negative = False
            self.is_infinity = False
            self.is_nan = True
            # I change both values to 0 because It easy for other method such as __add__, __mul__
            self.numerator = 0
            self.denominator = 0

        elif denominator == 0:
            if numerator > 0:
                self.is_negative = False
                self.is_infinity = True
                self.is_nan = False
            elif numerator == 0:
                self.is_negative = False
                self.is_infinity = False
                self.is_nan = True
            else:
                self.is_negative = True
                self.is_infinity = True
                self.is_nan = False

            if self.is_infinity:
                # Set new value for infinity
                self.numerator = 1
                self.denominator = 0
            elif self.is_nan:
                # Set new value for nan
                self.numerator = 0
                self.denominator = 0

        elif denominator in [math.inf, -math.inf]:
            # Set new value
            self.numerator = 0
            self.denominator = 1

            self.is_negative = False
            self.is_infinity = False
            self.is_nan = False

        elif numerator in [math.inf, -math.inf]:
            self.is_infinity = True
            self.is_nan = False
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
            self.is_nan = False

            if self.numerator / self.denominator >= 0:
                self.is_negative = False
            else:
                self.is_negative = True

        # round both parameter, (not nessary if both parameter are integer)
        if (not self.is_infinity) and (not self.is_nan):
            self.numerator = round(self.numerator)
            self.denominator = round(self.denominator)

        # Change fraction to the proper form
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
        # Strandard formula calculated
        numerator = self.numerator * frac.denominator + frac.numerator * self.denominator
        denominator = self.denominator * frac.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, frac):
        """ Return multiplication of two fractions as a new fraction
            use fomular, a/b * c/d = a*c / b*d
        """
        # Handle nan value
        if (self.__str__() == 'nan') or (frac.__str__() == 'nan'):
            return Fraction(0,0)
        # Handle infinity value
        if self.numerator * frac.numerator == 0 and self.denominator * frac.denominator == 0:
            if (self.__str__() in ['inf', '-inf']) and (frac.numerator == 0):
                return Fraction(0, 1)
            elif (frac.__str__() in ['inf', '-inf']) and (self.numerator == 0):
                return Fraction(0, 1)
        else:
            # Formular for calculate multiplication
            return Fraction(self.numerator * frac.numerator, self.denominator * frac.denominator)

    def __sub__(self, frac):
        """Return the subtraction of two fractions as a new fraction.
           Use the standard formula  a/b - c/d = (ad-bc)/(b*d)
        """
        # Strandard formula calculated
        numerator = self.numerator * frac.denominator - frac.numerator * self.denominator
        denominator = self.denominator * frac.denominator
        return Fraction(numerator, denominator)

    def __gt__(self, frac):
        """ Return the boolean True if fraction greather than parameter
        """

        # handle inf and nan
        if frac.__str__() == 'inf':
            return False
        if (frac.__str__() == 'nan') or (self.__str__() == 'nan'):
            return False
        elif (self.__str__() == 'inf') and (int(frac.__str__()) < math.inf):
            return True
        elif frac.__str__() == '-inf':
            if self.__str__() != '-inf':
                return True
            else:
                return False
        
        else:
            # standard formular for estimate two fractions
            return (self.numerator * frac.denominator) > (frac.numerator * self.denominator)

    def __neg__(self):
        """ Return a new Fraction as a negative 
            (positive if old fraction already negative)
            by change numerator variable to the negative
        """
        return Fraction(-self.numerator, self.denominator)

    def __str__(self):
        """ Return the result of this Fraction as a proper form
        """
        if self.numerator == 0:
            if self.denominator == 0:
                # If 0/0 show nan
                return f'{math.nan}'
            else:
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