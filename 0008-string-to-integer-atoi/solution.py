class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""

        for ch in s.strip():
            if ch.isdigit() or (ch in "+-" and num == ""):
                num += ch
            else:
                break

        if num == "" or num == "+" or num == "-":
            return 0

        ans = int(num)

        if ans > 2147483647:
            return 2147483647

        if ans < -2147483648:
            return -2147483648

        return ans
