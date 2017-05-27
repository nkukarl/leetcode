from unittest import TestCase

from nose_parameterized import parameterized

from rotate_image import Solution


class TestRotateImage(TestCase):
    @parameterized.expand([
        [
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3],
            ],
        ],
    ])
    def test_rotate(self, matrix, rotated):
        # Setup
        sol = Solution()

        # Exercise
        sol.rotate(matrix)

        # Verify
        self.assertEqual(matrix, rotated)
