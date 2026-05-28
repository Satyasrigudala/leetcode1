class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ssum=0
        tsum=0
        for i in s:
            ssum+=ord(i)
        for j in t:
            tsum+=ord(j)
        z=tsum-ssum
        return chr(z)   

