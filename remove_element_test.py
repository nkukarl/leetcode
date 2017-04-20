import random
from unittest import TestCase

from remove_element import Solution


class TestRemoveElement(TestCase):
    def test_remove_element(self):
        # Setup
        sol = Solution()
        target = random.randint(1, 9)
        numbers = [x for x in range(1, 10)] + [target] * 3
        random.shuffle(numbers)

        # Exercise
        ans = sol.remove_element(numbers, target)

        # Verify
        self.assertEqual(ans, 8)
