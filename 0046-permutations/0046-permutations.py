class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(curr_path, visited):
            # Base case: if the current permutation is complete
            if len(curr_path) == len(nums):
                res.append(curr_path.copy())
                return
            
            # Explore choices
            for num in nums:
                if num not in visited:
                    # Choose
                    visited.add(num)
                    curr_path.append(num)
                    
                    # Explore
                    backtrack(curr_path, visited)
                    
                    # Unchoose (Backtrack)
                    curr_path.pop()
                    visited.remove(num)
                    
        backtrack([], set())
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna