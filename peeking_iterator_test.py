from unittest import TestCase

from nose_parameterized import parameterized

from peeking_iterator import PeekingIterator


class Iterator(object):
    def __init__(self, nums):
        self.nums = nums[::-1]

    def has_next(self):
        return len(self.nums) > 0

    def get_next(self):
        return self.nums.pop()


class TestPeekingIterator(TestCase):
    @parameterized.expand([
        [
            [],
        ],
        [
            [1, 2, 3, 4, 5]
        ],
    ])
    def test_peeking_iterator(self, nums):
        # Setup
        iterator = Iterator(nums)
        peeking_iterator = PeekingIterator(iterator)

        # Exercise and Verify
        index = 0
        while peeking_iterator.has_next():
            peek_ = peeking_iterator.peek()
            next_ = peeking_iterator.get_next()
            self.assertEqual(peek_, nums[index])
            self.assertEqual(next_, nums[index])
            index += 1
