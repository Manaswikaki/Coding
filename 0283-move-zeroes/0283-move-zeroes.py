class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_element_at = 0
        
        # Step 1: Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_element_at] = nums[i]
                last_non_zero_element_at += 1
                
        # Step 2: Fill the remaining indices with zeroes
        for i in range(last_non_zero_element_at, len(nums)):
            nums[i] = 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna