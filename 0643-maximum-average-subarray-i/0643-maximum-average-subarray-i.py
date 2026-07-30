class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Step 1: Calculate the sum of the first window of size k
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Step 2: Slide the window across the rest of the array
        for i in range(k, len(nums)):
            # Add the new element entering the window
            # Subtract the old element leaving the window
            current_sum += nums[i] - nums[i - k]
            
            # Update the maximum sum found so far
            if current_sum > max_sum:
                max_sum = current_sum
                
        # Step 3: Return the maximum average
        return max_sum / k


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna