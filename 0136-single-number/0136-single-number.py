from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts=Counter(nums)
        l=min(counts, key=counts.get)
        return l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna