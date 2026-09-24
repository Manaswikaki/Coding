class Solution:
    def matrixMultiplication(self, arr):
        # n is the total number of matrices
        n = len(arr) - 1
        
        # If there is only one matrix, no multiplication is needed
        if n <= 1:
            return 0
            
        # dp[i][j] stores the minimum multiplication cost for matrices from index i to j
        dp = [[0] * n for _ in range(n)]
        
        # l represents the length of the chain of matrices being considered
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = float('inf')
                
                # Try placing the parenthesis at every possible split point k
                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + arr[i] * arr[k+1] * arr[j+1]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        
        # Return the minimum cost to multiply the entire chain from 0 to n-1
        return dp[0][n-1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna