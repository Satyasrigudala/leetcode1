class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=0
        maxi=nums[0]
        for i in range(1,len(nums)):
            res=max(res,(maxi-1)*(nums[i]-1))
            maxi=max(maxi,nums[i])
        return res   
