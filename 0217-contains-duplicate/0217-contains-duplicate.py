class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=list(set(nums))
        if len(nums) != len(a):
            return True
        else:
            return False 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna