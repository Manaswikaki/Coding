class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        # Sort words by length because a predecessor must be shorter
        words.sort(key=len)
        
        # dp dictionary stores the longest chain ending at each word
        dp = {}
        max_chain = 1
        
        for word in words:
            dp[word] = 1  # Base case: every word is a chain of length 1
            
            # Generate all possible predecessors by removing 1 character
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                
                # If the predecessor is in our list of known words, update the chain length
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            
            # Keep track of the global maximum chain length found
            max_chain = max(max_chain, dp[word])
            
        return max_chain


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna