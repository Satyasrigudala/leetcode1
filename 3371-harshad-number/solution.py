class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=0
        p=0
        n=x
        for d in str(x):
            s=s+int(d)
        if n % s==0:
            return s
        else:
            return -1
