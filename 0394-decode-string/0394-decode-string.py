class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the multi-digit multiplier
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push context: (previously built string, multiplier for the new bracket)
                stack.append((current_string, current_num))
                # Reset tracking variables for inside the bracket
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop context from the stack
                last_string, num = stack.pop()
                # Decode the bracket contents and append to previous context
                current_string = last_string + (current_string * num)
            else:
                # Regular lowercase character
                current_string += char
                
        return current_string


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna