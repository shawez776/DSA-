#brute force solution 
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         low, high = 0 , n-1
#         for i in range(0,n):
#             if nums[i] == target:
#                 return i 
#         return -1
        

#optimal solution (using binary search as it is sorted array)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the right half is sorted
            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            # Otherwise, the left half must be sorted
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
        return -1
