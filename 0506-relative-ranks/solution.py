class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = score.copy()
        temp.sort(reverse=True)

        ans = [""] * len(score)

        for i in range(len(temp)):
            pos = score.index(temp[i])

            if i == 0:
                ans[pos] = "Gold Medal"
            elif i == 1:
                ans[pos] = "Silver Medal"
            elif i == 2:
                ans[pos] = "Bronze Medal"
            else:
                ans[pos] = str(i + 1)

        return ans
        
        
