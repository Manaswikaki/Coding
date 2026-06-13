class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0
        
        for num in nums:
            if num == 1:
                current_ones += 1
                # Update max_ones if current streak is larger
                if current_ones > max_ones:
                    max_ones = current_ones
            else:
                # Reset current streak when a 0 is encountered
                current_ones = 0
                
        return max_ones


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna