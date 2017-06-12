from unittest import TestCase

from nose_parameterized import parameterized

from valid_triangle_number import Solution


class TestValidTriangleNumber(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [
                    2, 2, 3, 4,
                ],
            },
        ],
        [
            {
                'nums': [
                    91, 36, 26, 41, 21, 34, 58, 14, 49, 11, 68, 35, 61, 84, 78,
                    69, 58, 22, 43, 13, 49, 36, 70, 29, 27, 59, 94, 99, 25, 56,
                    95, 5, 67, 42, 33, 71, 40, 91, 51, 87, 79, 10, 39, 43, 45,
                    66, 31, 96, 73, 68, 25, 12, 84, 30, 86, 49, 72, 79, 44, 56,
                    61, 9, 25, 86, 46, 74, 96, 92, 63, 32, 72, 30, 82, 2, 32,
                    50, 91, 65, 78, 14, 30, 98, 30, 43, 57, 81, 28, 51, 84, 86,
                    36, 78, 19, 43, 62, 88, 100, 55, 68, 41,
                ],
            },
        ],
        [
            {
                'nums': [
                    100, 67, 86, 33, 77, 11, 29, 21, 8, 67, 36, 90, 46, 25, 53,
                    44, 27, 91, 76, 38, 5, 76, 30, 33, 34, 79, 59, 94, 18, 34,
                    95, 32, 0, 80, 38, 26, 5, 91, 30, 86, 17, 28, 88, 97, 66, 6,
                    5, 21, 86, 3, 5, 30, 84, 33, 6, 90, 12, 57, 29, 71, 25, 68,
                    45, 3, 80, 55, 73, 6, 31, 65, 20, 1, 55, 40, 87, 52, 59, 92,
                    52, 55, 32, 95, 5, 95, 33, 65, 31, 89, 94, 83, 56, 69, 94,
                    79, 36, 43, 82, 18, 43, 80,
                ],
            },
        ],
        [
            {
                'nums': [
                    11, 25, 92, 88, 22, 74, 16, 10, 82, 57, 62, 19, 96, 97, 53,
                    95, 38, 89, 22, 99, 69, 45, 74, 93, 41, 25, 14, 63, 83, 85,
                    9, 5, 66, 50, 50, 2, 94, 15, 28, 82, 14, 23, 17, 0, 43, 25,
                    16, 68, 16, 52, 18, 59, 26, 41, 2, 87, 47, 51, 26, 42, 3,
                    100, 21, 7, 23, 4, 21, 20, 21, 82, 77, 40, 41, 43, 87, 24,
                    70, 59, 71, 55, 78, 9, 66, 58, 96, 84, 58, 50, 78, 88, 63,
                    53, 94, 87, 84, 80, 66, 90, 11, 91,
                ],
            },
        ],
    ])
    def test_triangle_number(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.triangle_number(**kwargs)

        # Verify
        expected_ans = self.triangle_number(**kwargs)
        self.assertEqual(ans, expected_ans)

    def triangle_number(self, nums):
        self.cache_valid = set()
        self.cache_invalid = set()
        self.count = 0

        self.explore(nums, [])
        return self.count

    def explore(self, nums, cur):
        if 3 == len(cur):
            cur = tuple(sorted(cur))
            if cur in self.cache_valid:
                self.count += 1
                return
            elif cur in self.cache_invalid:
                return
            is_valid = self.is_valid_triplet(cur)
            if is_valid:
                self.count += 1
                self.cache_valid.add(cur)
            else:
                self.cache_invalid.add(cur)
        else:
            for i, n in enumerate(nums):
                self.explore(nums[i + 1:], cur + [n])

    def is_valid_triplet(self, sides):
        a, b, c = sides
        return a + b > c and abs(a - b) < c