class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    # If looking for the first occurrence, narrow search to the left
                    if is_first:
                        right = mid - 1
                    # If looking for the last occurrence, narrow search to the right
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        return [find_bound(is_first=True), find_bound(is_first=False)]
