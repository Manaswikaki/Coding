class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Find the maximum value to size our DP array
        max_val = max(nums)
        
        # Aggregate points gained from each number
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
            
        # House Robber dynamic programming approach
        prev_max = 0  # Max points from the previous step (i - 2)
        curr_max = 0  # Max points including the current step (i - 1)
        
        for p in points:
            # At each number, decide to either take it (plus prev_max) or skip it (keep curr_max)
            prev_max, curr_max = curr_max, max(curr_max, prev_max + p)
            
        return curr_max


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna