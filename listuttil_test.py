import unittest
from listutil import unique


class UniqueTest(unittest.TestCase):
    """ Test for 'unique' function in 'listutil' file """
    def test_empty_list(self):
        self.assertEqual([], unique([]))

    def test_one_item(self):
        self.assertEqual([5], unique([5]))
        self.assertEqual(['A'], unique(['A']))
        self.assertEqual([3.14], unique([3.14]))

    def test_one_item_many_times(self):
        self.assertEqual([1], unique([1, 1, 1, 1]))
        self.assertEqual(['A'], unique(['A', 'A', 'A', 'A', 'A']))
        self.assertEqual([1.14], unique([1.14, 1.14]))

    def test_two_item_many_times_orders(self):
        self.assertEqual([1, 2], unique([1,2,1,2,1]))
        self.assertEqual([2, 1], unique([2,2,1,1,2]))


if __name__ == '__main__':
    unittest.main()