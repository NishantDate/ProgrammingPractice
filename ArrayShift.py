class Solution:
    def rotate(self, nums, k: int) -> None:
        new_start = k%len(nums)
        new_nums = [None] * len(nums)
        new_end = new_start - 1
        new_nums[new_start:] = nums[0: (len(nums) - new_start)]
        new_nums[0: new_end + 1] = nums[(len(nums) - new_start):]
        print(f"{nums[(len(nums) - new_start):]} some more nums")
        return new_nums
