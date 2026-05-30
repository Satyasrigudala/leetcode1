class Solution:
    def reverseWords(self, s: str) -> str:
        result=[]
        l=s.split()
        for word in l:
            result.append(word[::-1])
        return " ".join(result) 
        
