class Solution:
    def rotate(self, nums, k: int) -> None:
        new_start = k%len(nums)
        new_nums = [None] * len(nums)
        new_end = new_start - 1
        new_nums[new_start:] = nums[0: (len(nums) - new_start)]
        new_nums[0: new_end + 1] = nums[(len(nums) - new_start):]
        print(f"{nums[(len(nums) - new_start):]} some more nums")
        return new_nums

    def moveZeroes(self, nums) -> None:
        non_zeroes = []
        zeroes = []
        while(len(nums)):
            if nums[0] == 0:
                zeroes.append(nums.pop(0))
            else:
                non_zeroes.append(nums.pop(0))
        return non_zeroes + zeroes

    def twoSum(self, numbers, target: int):
        numSet = {}
        ret = []
        i = 0
        least = numbers[0]
        while numbers[i] + least <= target
            if (target - numbers[i]) in numSet.keys():
                ret.append(numSet[target - numbers[i]])
                ret.append(i + 1)
            else:
                numSet[numbers[i]] = i + 1
            i += 1
            if i >= len(numbers):
                break
        return ret

    def reverseString(self, s: List[str]) -> None:
        end = len(s) - 1
        start = 0 
        
        while(end >= start):
            s[end], s[start] = s[start], s[end]
            
            end -= 1
            start += 1

