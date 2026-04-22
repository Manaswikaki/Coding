class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] will store the least number of perfect squares that sum to i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Precompute square numbers up to n
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                # The count for i is 1 + the count for (i - square)
                dp[i] = min(dp[i], dp[i - square] + 1)
                
        return dp[n]
