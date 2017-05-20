from unittest import TestCase

from range_sum_query import NumArray


class TestRangeSumQuery(TestCase):
    def test_num_array(self):
        # Setup
        num_array = NumArray([1, 3, 5, 7])

        # Exercise and Verify
        self.assertEqual(num_array.sum_range(0, 2), 9)
        num_array.update(1, 2)
        self.assertEqual(num_array.sum_range(0, 2), 8)
        self.assertEqual(num_array.sum_range(0, 3), 15)
        num_array.update(3, 2)
        self.assertEqual(num_array.sum_range(0, 3), 10)
