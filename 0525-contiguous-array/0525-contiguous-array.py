class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # Map to store the first occurrence of a running sum
        # Base case: A sum of 0 occurs at index -1
        sum_indices = {0: -1}
        
        max_length = 0
        running_sum = 0
        
        for i, num in enumerate(nums):
            # Change 0 to -1, keep 1 as 1
            running_sum += 1 if num == 1 else -1
            
            # If this sum has been seen before, calculate the distance
            if running_sum in sum_indices:
                subarray_length = i - sum_indices[running_sum]
                max_length = max(max_length, subarray_length)
            else:
                # Store the first time we see this running sum
                sum_indices[running_sum] = i
                
        return max_length


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna