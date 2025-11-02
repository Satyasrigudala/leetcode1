class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:              # Repeat until single digit
            sum_digits = 0
            for digit in str(num):    # Add all digits
                sum_digits += int(digit)
            num = sum_digits
        return num
        
