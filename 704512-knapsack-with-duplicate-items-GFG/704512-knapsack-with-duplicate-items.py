class Solution:
    def knapSack(self, val, wt, capacity):
        # Initialize DP table where dp[w] stores max profit at capacity w
        dp = [0] * (capacity + 1)

        # Iterate through all capacities from 1 to capacity
        for w in range(1, capacity + 1):
            # Try every item for the current capacity
            for i in range(len(wt)):
                if wt[i] <= w:
                    dp[w] = max(dp[w], val[i] + dp[w - wt[i]])

        return dp[capacity]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna