class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Define the binary search boundary range
        low = max(nums)
        high = sum(nums)
        ans = high
        
        # Helper function to check validity of a target max sum
        def canSplit(max_sum: int) -> bool:
            subarray_count = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > max_sum:
                    # Start a new subarray
                    subarray_count += 1
                    current_sum = num
                else:
                    current_sum += num
                    
            # Return True if we didn't exceed the allowed k subarrays
            return subarray_count <= k

        # Execute binary search
        while low <= high:
            mid = (low + high) // 2
            
            if canSplit(mid):
                ans = mid       # Track the viable minimized largest sum
                high = mid - 1  # Try to find a smaller valid maximum sum
            else:
                low = mid + 1   # Increase the allowed sum threshold
                
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna