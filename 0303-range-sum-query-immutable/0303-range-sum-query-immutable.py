class NumArray:

    def __init__(self, nums: List[int]):
        # Initialize prefix sum array with an extra 0 at the beginning
        self.prefix = [0] * (len(nums) + 1)
        
        # Fill the prefix sums
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the range sum in O(1) time
        return self.prefix[right + 1] - self.prefix[left]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna