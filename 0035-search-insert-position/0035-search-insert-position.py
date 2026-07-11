class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x=len(nums)
        for i in range(x):
            if target in nums:
                if nums[i]==target:
                    return i
            else:
                if nums[x-1]<target:
                    return x
                else:
                    if nums[i]>target:
                        return i
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna