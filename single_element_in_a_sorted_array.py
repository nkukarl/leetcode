class Solution(object):
    def single_non_duplicate(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (right - left + 1) % 4 == 1:
                if nums[mid] == nums[mid - 1]:
                    right = mid
                elif nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    # A number which is not equal to its left nor right
                    # is a single number.
                    return nums[mid]
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    right = mid - 1
                else:
                    return nums[mid]
        return nums[left]
