class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle the edge case for overflow: -2^31 / -1 results in 2^31, which is out of range.
        if dividend == -2147483648 and divisor == -1:
            return 2147483647 #

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Take absolute values of dividend and divisor using negation to avoid issues with abs(-2^31) in Python
        # which can overflow to a positive number larger than the max positive int
        a = -abs(dividend)
        b = -abs(divisor)

        quotient = 0
        # Perform division using bit manipulation (repeated subtraction with doubling)
        while a <= b:
            temp = b
            count = 1
            # Double 'temp' (divisor) as long as it fits into the remaining 'a' (dividend)
            while temp >= (-(2**30)) and a <= (temp << 1):
                temp <<= 1
                count <<= 1
            
            a -= temp # Subtract the largest possible multiple
            quotient += count # Add the corresponding count to the quotient

        # Apply the correct sign and ensure it stays within the 32-bit integer range
        if not negative:
            # Check for overflow if the result should be positive
            return min(quotient, 2147483647) 
        else:
            return -quotient
