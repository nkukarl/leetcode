import random
from unittest import TestCase

from nose_parameterized import parameterized

from remove_element import Solution


class TestRemoveElement(TestCase):
    def test_remove_element_dynamically_generated(self):
        # Setup
        sol = Solution()
        val = random.randint(1, 9)
        nums = [x for x in range(1, 10)] + [val] * 3
        random.shuffle(nums)

        # Exercise
        ans = sol.remove_element(nums, val)

        # Verify
        self.assertEqual(ans, 8)

    @parameterized.expand([
        [
            {
                'nums': [],
                'val': 1,
            },
            0,
        ],
        [
            {
                'nums': [1],
                'val': 1,
            },
            0,
        ],
        [
            {
                'nums': [1, 1],
                'val': 1,
            },
            0,
        ],
        [
            {
                'nums': [1, 2, 1],
                'val': 1,
            },
            1,
        ]
    ])
    def test_remove_element(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.remove_element(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
