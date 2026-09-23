class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n = len(val)
        # Initialize a DP table to store the maximum value for each capacity up to W
        dp = [0] * (W + 1)

        # Iterate over all items
        for i in range(n):
            # Iterate backwards through capacities to prevent using the same item multiple times
            for w in range(W, wt[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - wt[i]] + val[i])

        return dp[W]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna