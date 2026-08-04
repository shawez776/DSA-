class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #noor
        # pos= []
        # neg= []
        # for i in range (0, len(nums)):
        #     if nums[i]<0:
        #         neg.append(nums[i])
        #     else:
        #         pos.append(nums[i])

        # for i in range (0,len(pos)):
        #     nums[2*i] = pos[i]
        #     nums[2*i+1] = neg[i]

        # return nums

        pos = []
        neg= []
        n = len(nums)
        res = [0] * n
        pos_index, neg_index = 0,1 

        for i in range (0,n):
            if nums[i]>=0:
                res[pos_index] = nums[i]
                pos_index+=2
            else:
                res[neg_index] = nums[i]
                neg_index+=2

        return res
