class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(index: int, current_combination: List[int], current_sum: int):
            # Base Case: Found a combination that matches the target
            if current_sum == target:
                result.append(list(current_combination))
                return
            
            # Base Case: Exceeded target or ran out of candidates
            if current_sum > target or index >= len(candidates):
                return
            
            # Choice 1: Include the current candidate (we don't increment index to allow reuse)
            current_combination.append(candidates[index])
            backtrack(index, current_combination, current_sum + candidates[index])
            current_combination.pop() # Backtrack
            
            # Choice 2: Skip the current candidate and move to the next one
            backtrack(index + 1, current_combination, current_sum)
            
        backtrack(0, [], 0)
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna