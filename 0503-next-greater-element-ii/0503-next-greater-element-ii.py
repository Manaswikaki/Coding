class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # Stores indices
        
        # Iterate twice over the array to simulate circular behavior
        for i in range(2 * n):
            num = nums[i % n]
            
            # Pop elements from stack if current element is greater
            while stack and nums[stack[-1]] < num:
                pop_idx = stack.pop()
                res[pop_idx] = num
                
            # Only push indices from the first pass to avoid redundancy
            if i < n:
                stack.append(i)
                
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna