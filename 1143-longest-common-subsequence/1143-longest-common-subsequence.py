class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # Create a 2D DP table initialized with 0
        # dp[i][j] represents the LCS length of text1[0...i-1] and text2[0...j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the DP table bottom-up
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match: add 1 to the previous diagonal state
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Characters do not match: take the maximum from top or left
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[m][n]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna