import unittest
from formalgrammar.utils import utils


class TestPartition(unittest.TestCase):
    def test_partition(self):
        ls = [1, 2, 3]
        expected_result = [[[1, 2, 3]], [[1], [2, 3]], [[1, 2], [3]],
                           [[2], [1, 3]], [[1], [2], [3]]]
        self.assertEqual(list(utils.partition(ls)), expected_result)

    def test_filter_subsets(self):
        ls = [[[1, 2, 3]], [[1], [2, 3]], [[1, 2], [3]],
              [[2], [1, 3]], [[1], [2], [3]]]
        expected_result0 = [[[1], [2, 3]], [[1, 2], [3]],
                            [[2], [1, 3]], [[1], [2], [3]]]
        expected_result1 = [[[1], [2], [3]]]
        filtered0 = list(utils.filter_subsets(ls, 3))
        filtered1 = list(utils.filter_subsets(ls, 2))
        self.assertEqual(filtered0, expected_result0)
        self.assertEqual(filtered1, expected_result1)

    def test_filter_unordered_subsets(self):
        ls = [[[1, 2, 3]], [[1], [2, 3]], [[1, 2], [3]],
              [[2], [1, 3]], [[1], [2], [3]]]
        expected_result = [[[1, 2, 3]], [[1], [2, 3]], [[1, 2], [3]],
                           [[1], [2], [3]]]
        filtered = list(utils.filter_unordered_subsets(ls))
        self.assertEqual(filtered, expected_result)
