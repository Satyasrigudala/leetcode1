class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1  # map number → index
            if nums[index] > 0:
                nums[index] = -nums[index]  # mark as visited

        # Collect numbers not visited
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
