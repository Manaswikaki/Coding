class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def backtrack(start: int, path: List[str]):
            # Base case: reached the end of the string
            if start == len(s):
                result.append(list(path))
                return
            
            # Explore all possible substrings starting at 'start'
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # Check if the current substring is a palindrome
                if substring == substring[::-1]:
                    path.append(substring)     # Choose
                    backtrack(end, path)       # Explore
                    path.pop()                 # Unchoose (Backtrack)
                    
        backtrack(0, [])
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna