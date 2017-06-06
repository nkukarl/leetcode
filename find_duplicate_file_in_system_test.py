from unittest import TestCase

from nose_parameterized import parameterized

from find_duplicate_file_in_system import Solution


class TestFindDuplicateFileInSystem(TestCase):
    @parameterized.expand([
        [
            {
                'paths': [
                    'root/a 1.txt(abcd) 2.txt(efgh)', 'root/c 3.txt(abcd)',
                    'root/c/d 4.txt(efgh)', 'root 4.txt(efgh)',
                ],
            },
            [
                ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt'],
                ['root/a/1.txt', 'root/c/3.txt'],
            ],
        ],
        [
            {
                'paths': [
                    "root/a 1.txt(abcd) 2.txt(efsfgh)", "root/c 3.txt(abdfcd)",
                    "root/c/d 4.txt(efggdfh)",
                ],
            },
            [],
        ]
    ])
    def test_find_duplicate(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_duplicate(**kwargs)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
