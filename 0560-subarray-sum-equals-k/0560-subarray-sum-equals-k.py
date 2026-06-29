class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        # prefix_sums stores {prefix_sum : frequency}
        prefix_sums = {0: 1}
        
        for num in nums:
            curr_sum += num
            
            # Check if (curr_sum - k) exists in our map
            if (curr_sum - k) in prefix_sums:
                count += prefix_sums[curr_sum - k]
            
            # Update the frequency of the current prefix sum
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            
        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna