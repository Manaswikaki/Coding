class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # Initialize an array of size amount + 1 with 0s
        # dp[i] will store the number of combinations to make up amount i
        dp = [0] * (amount + 1)
        
        # Base case: There is exactly 1 way to make an amount of 0 (by choosing no coins)
        dp[0] = 1
        
        # Iterate through each coin denomination
        for coin in coins:
            # Update the dp array for all amounts that can include this coin
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                
        return dp[amount]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna