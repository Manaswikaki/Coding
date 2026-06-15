class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        
        for n in nums:
            # If current_sum becomes negative, reset it to 0
            if current_sum < 0:
                current_sum = 0
            
            current_sum += n
            # Update max_sum if the new current_sum is larger
            max_sum = max(max_sum, current_sum)
            
        return max_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna