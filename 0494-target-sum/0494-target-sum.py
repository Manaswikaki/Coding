class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Check if a valid partition is possible
        if (target + total_sum) % 2 != 0 or total_sum < abs(target):
            return 0
            
        subset_sum = (target + total_sum) // 2
        
        # dp[i] stores the number of ways to form a subset with sum i
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # Base case: 1 way to get a sum of 0 (empty subset)
        
        # Bottom-up 1D Dynamic Programming
        for num in nums:
            # Traverse backwards to avoid using the same element multiple times
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]
                
        return dp[subset_sum]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna