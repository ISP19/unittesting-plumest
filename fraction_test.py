import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        """ Test did __str__ show an output correct. """
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        # more test case
        self.assertEqual('1000', Fraction(1000, 1))
        self.assertEqual('1/2', Fraction(-1, -2))
        self.assertEqual('inf', Fraction(5, 0))
        self.assertEqual('-inf', Fraction(-1, 0))
        self.assertEqual('0', Fraction(9, -math.inf))
        self.assertEqual('0', Fraction(-3, math.inf))
        self.assertEqual('-inf', Fraction(math.inf, -1))
        self.assertEqual('inf', Fraction(math.inf, 100))

   
    def test_add(self):
        """ Test did __add__ calculate correct. """
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(1,12), Fraction(1,12)+Fraction(0,3))
        self.assertEqual(Fraction(-5,6), Fraction(1,-2)+Fraction(-1,3))
        self.assertEqual(Fraction(1,4), Fraction(3,4)+Fraction(-2,4))
        self.assertEqual(Fraction(3), Fraction(1,2)+Fraction(5,2))
        self.assertEqual(Fraction(37,60), Fraction(2,12)+Fraction(45,100))
        self.assertEqual(Fraction(math.inf), Fraction(1,0)+Fraction(1,2))
        self.assertEqual(math.inf, Fraction(1,0)+Fraction(-1000))
        self.assertEqual(-math.inf, Fraction(-1,0)+Fraction(1000))
    
    
    def test_sub(self):
        """ Test did __sub__ calculate correct. """
        self.assertEqual(Fraction(-7,12), Fraction(1,12)-Fraction(2,3))
        self.assertEqual(Fraction(1,12), Fraction(1,12)-Fraction(0,3))
        self.assertEqual(Fraction(0,12), Fraction(1,12)-Fraction(1,12))
        self.assertEqual(Fraction(2), Fraction(1,4)-Fraction(-7,4))
        self.assertEqual(Fraction(1, 72), Fraction(1,8)-Fraction(1,9))
        self.assertEqual(Fraction(math.inf), Fraction(1,0)-Fraction(1,2))
        self.assertEqual(Fraction(1, 0), Fraction(1,0)-Fraction(-1000))
        self.assertEqual(Fraction(-1,0), Fraction(-1,0)-Fraction(1000))

    def test_init(self):
        """ Test did the class throw an error """
        with self.assertRaises(TypeError):
            Fraction('s')
        with self.assertRaises(TypeError):
            Fraction('hi', 'there!')
        with self.assertRaises(ValueError):
            Fraction(0, 0)
        with self.assertRaises(ValueError):
            Fraction(-math.inf, math.inf)

    def test_eq(self):
        """ Test did __eq__ show correct boolean. """
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        # Consider special values like 0, 1/0, -1/0
        self.assertTrue(Fraction(1, 0) == Fraction(math.inf))
        self.assertTrue(Fraction(-1, 0) == Fraction(-math.inf))
        self.assertTrue(Fraction(0) == Fraction(-100, -math.inf))

    def test_mul(self):
        """ Test did __mul__ calculate correct. """
        self.assertEqual(Fraction(3,10), Fraction(1,2) * Fraction(3,5))
        self.assertEqual(Fraction(0), Fraction(1,2) * Fraction(0))
        self.assertEqual(Fraction(3,4), Fraction(1,2) * Fraction(3,2))
        self.assertEqual(Fraction(1,0), Fraction(1,0) * Fraction(1,3))
        self.assertEqual(Fraction(-1,0), Fraction(1,0) * Fraction(1,-5))
        self.assertEqual(Fraction(0,1), Fraction(1,0) * Fraction(0,-50))
        self.assertEqual(Fraction(0,1), Fraction(0,1) * Fraction(10,0))

    def test_neg(self):
        """ Test did __neg__ change the fraction to negative
            (positive if fraction are negative already) """
        self.assertEqual('-1/2', Fraction(1, 2).__neg__())
        self.assertEqual('1/2', Fraction(1, -2).__neg__())
        self.assertEqual('1/2', Fraction(-1, 2).__neg__())
        self.assertEqual('-1/2', Fraction(-1, -2).__neg__())
        self.assertEqual('0', Fraction(0, 15).__neg__())
        self.assertEqual('-inf', Fraction(1, 0).__neg__())
        self.assertEqual('inf', Fraction(-1, 0).__neg__())

    def test_gt(self):
        """ Test did __gt__ return boolean True when it greater,
            False when otherwise
        """
        self.assertTrue(Fraction(1, 0) > Fraction(0))
        self.assertTrue(Fraction(1, 2) > Fraction(4, 16))
        self.assertTrue(Fraction(0) > Fraction(-1, 256))
        self.assertFalse(Fraction(0) > Fraction(1, 49))
        self.assertFalse(Fraction(1, 0) > Fraction(1, 0))
        self.assertFalse(Fraction(1, -2) > Fraction(-1, 10))


if __name__ == '__main__':
    """ Run unittest in all method. """
    unittest.main()