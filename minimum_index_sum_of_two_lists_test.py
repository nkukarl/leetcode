from unittest import TestCase

from nose_parameterized import parameterized

from minimum_index_sum_of_two_lists import Solution


class TestMinimumIndexSumOfTwoLists(TestCase):
    @parameterized.expand([
        [
            {
                'list1': [
                    'Shogun', 'Tapioca Express', 'Burger King', 'KFC',
                ],
                'list2': [
                    'Piatti', 'The Grill at Torrey Pines',
                    'Hungry Hunter Steakhouse', 'Shogun',
                ],
            },
        ],
    ])
    def test_find_restaurant(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_restaurant(**kwargs)

        # Verify
        expected_ans = self.find_restaurant(**kwargs)
        self.assertEqual(sorted(ans), sorted(expected_ans))

    def find_restaurant(self, list1, list2):
        summary1 = {rest: i for i, rest in enumerate(list1)}
        summary2 = {rest: i for i, rest in enumerate(list2)}

        summary = {}
        min_index_sum = len(list1) + len(list2)
        for rest in set(list1) & set(list2):
            index_sum = summary1[rest] + summary2[rest]
            if index_sum <= min_index_sum:
                min_index_sum = index_sum
                summary[min_index_sum] = summary.get(min_index_sum, []) + [rest]

        return summary[min_index_sum]
