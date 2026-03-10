class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # dp[i][j] = min operations to convert word1[:i] to word2[:j]
        # We use (m+1) x (n+1) table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # base cases: transforming to/from empty string
        for i in range(m + 1):
            dp[i][0] = i  # delete all characters from word1[:i]
        for j in range(n + 1):
            dp[0][j] = j  # insert all characters to form word2[:j]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # no operation needed
                else:
                    insert = dp[i][j - 1] + 1     # insert word2[j-1] into word1
                    delete = dp[i - 1][j] + 1     # delete word1[i-1]
                    replace = dp[i - 1][j - 1] + 1  # replace word1[i-1] with word2[j-1]
                    dp[i][j] = min(insert, delete, replace)
        
        return dp[m][n]