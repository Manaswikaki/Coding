class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # If total sum is odd, we cannot partition it equally
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        bits = 1  # Represents that a sum of 0 is always possible
        
        for num in nums:
            bits |= bits << num
            
        # Check if the target bit is set
        return (bits >> target) & 1 == 1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna