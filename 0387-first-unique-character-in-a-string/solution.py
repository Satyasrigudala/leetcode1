class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = []

        for i in s:
            q.append(i)
            a = len(q)

            if s.count(q[a-1]) == 1:
                return a - 1

        return -1
