class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return an empty list if the input string is empty
        if not digits:
            return []
        
        # Map each digit to its corresponding letters on a phone keypad
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, current_combination: list):
            # If the current combination length matches digits length, a path is complete
            if index == len(digits):
                result.append("".join(current_combination))
                return
            
            # Get the letters mapped to the current digit
            possible_letters = phone_map[digits[index]]
            
            # Loop through each letter and move to the next digit index
            for letter in possible_letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()  # Backtrack step
                
        # Start backtracking from the first digit
        backtrack(0, [])
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna