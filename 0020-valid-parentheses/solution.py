class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:  # ch is a closing bracket
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
        return not stack
        
        
