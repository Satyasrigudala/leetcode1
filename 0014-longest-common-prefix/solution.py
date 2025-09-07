class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Find smallest and largest string in lexicographic order
        first, last = min(strs), max(strs)
        
        # Compare characters one by one
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]
        
        
