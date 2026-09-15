class Solution:
    def rob(self, nums: list[int]) -> int:
        # Base case: if there is only one house, rob it
        if len(nums) == 1:
            return nums[0]
        
        # Helper function to solve the linear House Robber problem
        def rob_linear(houses: list[int]) -> int:
            prev2, prev1 = 0, 0
            for money in houses:
                # Max money if we either skip this house or rob it
                prev2, prev1 = prev1, max(prev1, prev2 + money)
            return prev1

        # Return the max of robbing houses 0 to n-2 OR houses 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna