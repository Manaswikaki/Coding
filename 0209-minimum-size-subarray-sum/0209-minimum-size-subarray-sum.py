class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window from the left as long as the condition is met
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        # If min_length was never updated, no valid subarray exists
        return min_length if min_length != float('inf') else 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna