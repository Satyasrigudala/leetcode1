class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        for num in nums:
            if num%3!=0:
                c+=1
        return c        

        
