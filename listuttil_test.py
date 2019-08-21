import unittest
from listutil import unique


class UniqueTest(unittest.TestCase):
    """ Test for 'unique' function in 'listutil' file """

    def test_empty_list(self):
        """ Use assertListEqual to confirmed that 'unique' function return 'list' """
        self.assertListEqual([], unique([]))

    def test_one_item(self):
        """ Check did function list with 1 item. """
        self.assertListEqual([5], unique([5]))
        self.assertListEqual(['A'], unique(['A']))
        self.assertListEqual([3.14], unique([3.14]))

    def test_one_item_many_times(self):
        """ Check did function list with 1 item. """
        self.assertListEqual([1], unique([1, 1, 1, 1]))
        self.assertListEqual(['A'], unique(['A', 'A', 'A', 'A', 'A']))
        self.assertListEqual([1.14], unique([1.14, 1.14]))

    def test_two_item_many_times_orders(self):
        """ Check is funtion return list of two element 
            that is not the same element 
        """
        self.assertListEqual([1, 2], unique([1, 2, 1, 2, 1]))
        self.assertListEqual([1, 2], unique([1, 1, 1, 2, 2]))
        self.assertListEqual([1, 2], unique([1, 2, 2, 2, 1]))
        self.assertListEqual([1, 2], unique([1, 1, 1, 2, 1]))
        self.assertListEqual([2, 1], unique([2, 2, 1, 1, 2]))

    def test_one_nest_list(self):
        """ Check did funtion return one nested list 
            (no matter how much items in deeper list)
        """
        self.assertListEqual([[]], unique([[]]))
        self.assertListEqual([[3, 3, 0]], unique([[3, 3, 0]]))
        self.assertListEqual([['Cat', 'Bat']], unique([['Cat', 'Bat']]))

    def test_one_nest_list_many_times(self):
        """ Check did funtion return one nested list 
            (no matter how much items in deeper list) """
        self.assertListEqual([[]], unique([[], []]))
        self.assertListEqual([[1, 3]], unique([[1, 3], [1, 3]]))

    def test_two_nest_lists_many_times_orders(self):
        """ Check did function return two nested list that is not the same
        """
        self.assertListEqual([[1], [2]], unique([[1], [2], [1], [2]]))
        self.assertListEqual([[1], [2]], unique([[1], [1], [1], [2]]))
        self.assertListEqual([[1], [2]], unique([[1], [2], [2], [2]]))

    def test_parameter_is_not_list(self):
        """ Test did funtion raise an error """
        with self.assertRaises(TypeError):
            unique(5)
        with self.assertRaises(TypeError):
            unique('Hello')
        with self.assertRaises(TypeError):
            unique({'name': 'Plume', 'age': 20})
        with self.assertRaises(TypeError):
            unique(None)


if __name__ == '__main__':
    unittest.main()
