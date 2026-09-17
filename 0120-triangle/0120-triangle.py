class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Initialize DP array with the bottom row of the triangle
        dp = list(triangle[-1])
        
        # Move upwards from the second-to-last row down to the top row (index 0)
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # For each cell, add its value to the minimum of its two lower neighbors
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
                
        # The top element now holds the minimum path sum
        return dp[0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna