class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # check if goal is a rotation of s
        return goal in (s + s)
        
