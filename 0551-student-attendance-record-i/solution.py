class Solution:
    def checkRecord(self, s: str) -> bool:
        for i in s:
            if s.count('A')<2 and 'LLL'not in s:
                return True
            else:
                return False   
        
