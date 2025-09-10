class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # If lengths don't match, pattern can't hold
        if len(pattern) != len(words):
            return False
        
        mapping = {}
        
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            
            # Check if this pattern char already seen
            if p in mapping:
                if mapping[p] != w:   # Inconsistent mapping
                    return False
            else:
                if w in mapping.values():  # Word already mapped to another char
                    return False
                mapping[p] = w  # Create new mapping
        
        return True

