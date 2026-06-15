from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums)
        a=len(nums)
        for key, value in c.items():
            if ((a//2)+1) <= value:
                return key

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna