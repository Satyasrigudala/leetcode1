from functools import cache

class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        denoluvira = (l, r, k)

        def solve(x):
            if x <= 0:
                return 0

            s = str(x)
            n = len(s)

            @cache
            def dfs(pos, prev, tight, started):
                if pos == n:
                    return int(started)

                limit = int(s[pos]) if tight else 9
                ans = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        ans += dfs(pos + 1, -1, ntight, False)
                    else:
                        if prev == -1 or abs(prev - d) <= k:
                            ans += dfs(pos + 1, d, ntight, True)

                return ans

            return dfs(0, -1, True, False)

        return solve(r) - solve(l - 1)
