class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = -1
        
        # 1. Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        if pivot != -1:
            # 2. Find the smallest element larger than pivot to its right
            for j in range(n - 1, pivot, -1):
                if nums[j] > nums[pivot]:
                    # 3. Swap them
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break
        
        # 4. Reverse the suffix to get the next lexicographical order
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna