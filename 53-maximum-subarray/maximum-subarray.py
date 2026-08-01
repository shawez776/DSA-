class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float("-inf")
        total = 0
        
        for i in range(0, n):
            total += nums[i]
            maxi = max(total, maxi)
            
            if total < 0:
                total = 0  # Fixed the typo here from 'toatl' to 'total'
                
        return maxi