class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            # Check if the current element is greater than the next (with wrap-around)
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        
        # A sorted and rotated array has at most one "drop"
        return count <= 1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna