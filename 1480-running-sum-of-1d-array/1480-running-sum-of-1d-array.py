class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Iterate from the second element to the end of the array
        for i in range(1, len(nums)):
            # Add the previous element's running sum to the current element
            nums[i] += nums[i - 1]
        return nums


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna