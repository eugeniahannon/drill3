import unittest

# import the items to be tested
from p1 import surround, same_key_vals, add_gene_key, \
    first_and_last, is_odd



# This is called a "test case". You don't need to worry too much about it
# aside from knowing that it defines different things to test out to
# validate your code.
# Each one of the functions is a separate test.
# If you want to know further what's going on, check this out but don't be too
# overwhelmed: https://docs.python.org/3/library/unittest.html
class P1Test(unittest.TestCase):
    def test_surround(self):
        result = surround(['a', 'b'], 'c')
        self.assertSequenceEqual(result, ['c', 'a', 'b', 'c'])
        
        result = surround([1, True], {'a':False})
        self.assertSequenceEqual(result, [{'a':False}, 1, True, {'a':False}])

    def test_same_key_vals(self):
        result = same_key_vals({'a': 1, 'b' : 'b', 'c': 2, 'd': 'd'})
        self.assertSequenceEqual(result, ['b', 'd'])

        result = same_key_vals({1: 1, 'b' : 'b', 'c': False})
        self.assertSequenceEqual(result, [1, 'b'])

    def test_add_gene_key(self):
        result = add_gene_key({'a': 1})
        self.assertEqual(result, {'a': 1, 'gene': 'cool'})

        result = add_gene_key({'gene': 'butt', 'b': False})
        self.assertEqual(result, {'b': False})

    def test_first_and_last(self):
        result = first_and_last([1, 2, 3, 4, 5])
        self.assertSequenceEqual(result, [1, 5])

        result = first_and_last(['a', 'b', 'c', 'd', 'e'])
        self.assertSequenceEqual(result, ["a", "e"])

    def test_is_odd(self):
        result = is_odd(1)
        self.assertTrue(result, "Incorrect result for is_odd(1)")

        result = is_odd(-2)
        self.assertFalse(result, "Incorrect result for is_odd(-2)")

        result = is_odd(0)
        self.assertTrue(result, "Incorrect result for is_odd(0)")



if __name__ == '__main__':
    unittest.main()