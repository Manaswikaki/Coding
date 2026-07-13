from collections import Counter

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # Count the frequency of each element
        counts = Counter(nums)
        
        # Find and return the element with a count of 1
        for num, count in counts.items():
            if count == 1:
                return num


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna