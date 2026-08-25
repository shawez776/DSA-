from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #submitted by noor
        #this  code gives the position of lower bond also
        n = len(nums)
        lb = n  
        low = 0
        high = n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return lb
