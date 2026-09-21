class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Initialize a 2D array where dp[i][j] stores the edit distance
        # between the prefix word1[0...i-1] and word2[0...j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base Cases: Converting a string to an empty string requires deletions
        for i in range(m + 1):
            dp[i][0] = i
            
        # Base Cases: Converting an empty string to a string requires insertions
        for j in range(n + 1):
            dp[0][j] = j
            
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Characters do not match, take the minimum of 3 operations:
                    # dp[i-1][j]   -> Delete character from word1
                    # dp[i][j-1]   -> Insert character into word1
                    # dp[i-1][j-1] -> Replace character in word1
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    
        return dp[m][n]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna