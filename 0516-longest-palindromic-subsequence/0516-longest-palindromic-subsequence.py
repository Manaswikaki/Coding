class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Create a DP table where dp[i][j] stores the LPS length for s[i...j]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
            
        # Build the table bottom-up
        for length in range(2, n + 1):  # length of substring
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[0][n - 1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna