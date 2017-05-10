from unittest import TestCase

from nose_parameterized import parameterized

from queue_reconstruction_by_height import Solution


class TestQueueReconstructionByHeight(TestCase):
    @parameterized.expand([
        [
            {
                'people': [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
            },
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
        ],
    ])
    def test_reconstruct_queue(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.reconstruct_queue(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
