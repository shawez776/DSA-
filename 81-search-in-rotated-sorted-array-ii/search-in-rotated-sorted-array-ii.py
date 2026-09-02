class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return True
            #edge case for the repeted element 
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
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
                    
        return False