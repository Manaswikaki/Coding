class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize the DP table with a value greater than any possible answer
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0
        
        # Compute minimum coins for every amount from 1 to target amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        # If dp[amount] was not updated, it's impossible to form that amount
        return dp[amount] if dp[amount] <= amount else -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna