class Solution:
    def minLights(self, lights: List[int]) -> int:
        n = len(lights)

        
        ravelunico = lights[:]

        diff = [0] * (n + 1)

      
        for i, v in enumerate(ravelunico):
            if v > 0:
                l = max(0, i - v)
                r = min(n - 1, i + v)
                diff[l] += 1
                if r + 1 < n:
                    diff[r + 1] -= 1

        visible = [False] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            visible[i] = cur > 0

        ans = 0
        i = 0

        while i < n:
            if visible[i]:
                i += 1
            else:
                j = i
                while j < n and not visible[j]:
                    j += 1

                length = j - i
                ans += (length + 2) // 3  

                i = j

        return ans
