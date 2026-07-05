class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start, path):
            # Append the current subset to the result
            res.append(path[:])
            
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Move to the next element
                backtrack(i + 1, path)
                # Backtrack: remove nums[i] to explore other possibilities
                path.pop()
        
        backtrack(0, [])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna