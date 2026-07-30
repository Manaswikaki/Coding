class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_count = 0
        
        for right in range(len(nums)):
            # Expand the window: count zeros
            if nums[right] == 0:
                zero_count += 1
            
            # Shrink the window if zeros exceed k
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna