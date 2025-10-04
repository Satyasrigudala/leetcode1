class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = j = 0   # i -> child, j -> cookie
        count = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:   # cookie can satisfy child
                count += 1
                i += 1
                j += 1
            else:
                j += 1  # cookie too small, try next one
        
        return count
        
