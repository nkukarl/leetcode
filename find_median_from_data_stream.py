class MedianFinder(object):
    def __init__(self):
        self.nums = []

    def add_num(self, num):
        nums = self.nums
        if [] == nums or num >= nums[-1]:
            nums.append(num)
        elif num <= nums[0]:
            nums.insert(0, num)
        else:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            nums.insert(left, num)

    def find_median(self):
        nums = self.nums
        N = len(nums)
        if N % 2 != 0:
            return nums[N // 2]
        return (nums[N // 2 - 1] + nums[N // 2]) / 2.0
