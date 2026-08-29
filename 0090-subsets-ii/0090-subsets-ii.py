class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sort the array to place duplicate elements next to each other
        nums.sort()
        
        def backtrack(start: int, path: List[int]):
            # Append a copy of the current subset to the result
            res.append(list(path))
            
            for i in range(start, len(nums)):
                # If the current element is a duplicate of the previous element,
                # and it's not the first element in this recursive level, skip it.
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                # Include the current element
                path.append(nums[i])
                # Move to the next element
                backtrack(i + 1, path)
                # Backtrack by removing the element
                path.pop()
                
        backtrack(0, [])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna