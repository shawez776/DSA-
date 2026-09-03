class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        mini = float('inf')
        
        while low <= high:
            mid = (low + high) // 2
            
            # If the entire sub-array is sorted
            if nums[low] <= nums[high]:
                mini = min(mini, nums[low])
                break
                
            # Left side is sorted, minimum must be at low or in right side
            if nums[low] <= nums[mid]:
                mini = min(mini, nums[low])
                low = mid + 1
            # Right side is sorted, minimum is in the right side including mid
            else:
                mini = min(mini, nums[mid])
                high = mid - 1
                
        return mini
