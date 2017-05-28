class Solution(object):
    def find_restaurant(self, list1, list2):
        summary1 = {rest: i for i, rest in enumerate(list1)}
        MAX_INDEX_SUM = min_index_sum = len(list1) + len(list2)

        ans = []
        for j, rest in enumerate(list2):
            i = summary1.get(rest, MAX_INDEX_SUM)
            index_sum = i + j
            if index_sum < min_index_sum:
                min_index_sum = index_sum
                ans = [rest]
            elif index_sum == min_index_sum:
                ans.append(rest)

        return ans
