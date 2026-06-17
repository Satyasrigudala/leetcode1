class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
       if len(set(zip(s, t))) == len(set(s)) == len(set(t)):
           return True
       else:
           return False

            
            
        
