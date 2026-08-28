class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        first, second = 1, 2
        for _ in range(3, n + 1):
            first, second = second, first + second
            
        return second


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna