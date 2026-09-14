class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Initialize the base costs for the first two steps
        prev2 = cost[0]
        prev1 = cost[1]
        
        # Iterate through the rest of the steps
        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr
            
        # The top of the stairs can be reached from either of the last two steps
        return min(prev1, prev2)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna