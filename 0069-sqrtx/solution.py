class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:  # Handle 0 and 1 quickly
            return x

        l, r = 1, x
        while l <= r:
            m = (l + r) // 2
            msq = m * m
            if msq == x:
                return m
            elif msq < x:
                l = m + 1
            else:
                r = m - 1

        return r  # r will be the floor(sqrt(x))

