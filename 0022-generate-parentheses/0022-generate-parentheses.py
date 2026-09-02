class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: valid combination found
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Add an open parenthesis if allowed
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
            
            # Add a closed parenthesis if it matches an open one
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna