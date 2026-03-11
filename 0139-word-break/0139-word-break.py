from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max((len(w) for w in wordDict), default=0)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # empty string

        for i in range(1, n + 1):
            # Only need to check substrings of length up to max_len
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]