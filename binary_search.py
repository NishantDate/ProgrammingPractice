class BinarySearch:
    def search(self, nums, target: int) -> int:
        num_i = len(nums)//2
        old_len = len(nums)
        old_start = 0
        while old_len > old_start:
            if old_len - old_start == 1:
                if old_len < len(nums):
                    if nums[old_len] == target:
                          return old_len
                    elif nums[old_start] == target:
                        return old_start
                    else:
                        break
                else:
                    if nums[old_len - 1] == target:
                        return old_len - 1
                    elif nums[old_start] == target:
                        return old_start
                    else:
                        break

            if nums[num_i] < target:
                old_start = num_i
                num_i  = (old_start+ old_len)//2
            elif nums[num_i] > target:
                old_len = num_i
                num_i = old_len//2   
            else:
                return num_i
                
            
        return -1

class SearchInsert:
    def searchInsert(self, nums, target: int) -> int:
        
        #Edge Cases
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        
        start = 0
        end = len(nums)
        middle = end//2
        
        while end > start:
            if len(nums) == 1: end -= 1
            if end - start == 1:
                if target == nums[end]:
                    return end
                if target == nums[start]:
                    return start
                
                return end
            
            if target > nums[middle]:
                start = middle
                middle = (start + end) // 2
            elif target < nums[middle]:
                end = middle
                middle = (start + end) // 2
            else:
                return middle

