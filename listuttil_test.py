import unittest
from listutil import unique


class UniqueTest(unittest.TestCase):
    """ Test for 'unique' function in 'listutil' file """

    def test_empty_list(self):
        """ Use assertListEqual to confirmed that 'unique' function return 'list' """
        self.assertListEqual([], unique([]))

    def test_one_item(self):
        self.assertListEqual([5], unique([5]))
        self.assertListEqual(['A'], unique(['A']))
        self.assertListEqual([3.14], unique([3.14]))

    def test_one_item_many_times(self):
        self.assertListEqual([1], unique([1, 1, 1, 1]))
        self.assertListEqual(['A'], unique(['A', 'A', 'A', 'A', 'A']))
        self.assertListEqual([1.14], unique([1.14, 1.14]))

    def test_two_item_many_times_orders(self):
        self.assertListEqual([1, 2], unique([1, 2, 1, 2, 1]))
        self.assertListEqual([2, 1], unique([2, 2, 1, 1, 2]))

    def test_one_nest_list(self):
        self.assertListEqual([[]], unique([[]]))
        self.assertListEqual([[3, 3, 0]], unique([[3, 3, 0]]))
        self.assertListEqual([['Cat', 'Dog', 'Bat']],
                             unique([['Cat', 'Dog', 'Bat']]))

    def test_one_nest_list_many_times(self):
        self.assertListEqual([[], [0]], unique([[], [0], []]))
        self.assertListEqual([[1, 2, 3], [1, 3]], unique([[1, 2, 3], [1, 3], [1, 3]]))

    def test_many_nest_lists_many_times(self):
        self.assertListEqual([[[3], [0]], [4], [[2], [1]]], unique([[[3], [0]], [4], [[2], [1]], [[3], [0]]]))
        self.assertListEqual([1, [1, 2], [[1], [2]], [[[1, 2], 1], [1, 2, [1, [1, 2]]], 1]], unique([1, [1, 2], [[1], [2]], [[[1, 2], 1], [1, 2, [1, [1, 2]]], 1], [[1], [2]]]))

    def test_parameter_is_not_list(self):
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
