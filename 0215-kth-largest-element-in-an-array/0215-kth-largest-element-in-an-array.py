class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=sorted(nums)
        return a[-k]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna