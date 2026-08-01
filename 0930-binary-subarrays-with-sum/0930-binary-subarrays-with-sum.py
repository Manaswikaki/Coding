class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k: int) -> int:
            if k < 0:
                return 0
            
            left = 0
            current_sum = 0
            count = 0
            
            for right in range(len(nums)):
                current_sum += nums[right]
                
                # Shrink window if the sum exceeds k
                while current_sum > k:
                    current_sum -= nums[left]
                    left += 1
                
                # All subarrays ending at 'right' and starting from 'left' to 'right' are valid
                count += (right - left + 1)
                
            return count

        return atMost(goal) - atMost(goal - 1)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna