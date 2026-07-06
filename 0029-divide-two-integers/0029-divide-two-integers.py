class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit integer limits
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Handle overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values to simplify logic
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Bit manipulation approach (Binary Long Division)
        while dividend >= divisor:
            temp_divisor, count = divisor, 1
            # Shift divisor left (multiply by 2) until it's larger than dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1
            
            # Subtract the largest found multiple and add count to quotient
            dividend -= temp_divisor
            quotient += count

        return -quotient if negative else quotient


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna