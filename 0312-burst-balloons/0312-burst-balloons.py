class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # Add virtual boundaries of 1 at both ends to handle edge cases
        A = [1] + nums + [1]
        n = len(A)
        
        # dp[i][j] represents the max coins from bursting all balloons strictly between i and j
        dp = [[0] * n for _ in range(n)]
        
        # length is the distance between i and j
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                
                # Test every possible balloon k to be the LAST one burst in the open interval (i, j)
                for k in range(i + 1, j):
                    coins = A[i] * A[k] * A[j] + dp[i][k] + dp[k][j]
                    if coins > dp[i][j]:
                        dp[i][j] = coins
                        
        return dp[0][n - 1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna