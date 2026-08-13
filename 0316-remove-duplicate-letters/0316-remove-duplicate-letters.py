class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Track the last occurrence index of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()  # Track characters currently in the stack
        
        for i, char in enumerate(s):
            # Skip if the character is already in our result
            if char in seen:
                continue
                
            # Maintain monotonic increasing order if possible
            # Pop the character if:
            # 1. Stack is not empty
            # 2. Current char is smaller than the stack top (lexicographically better)
            # 3. The stack top character appears again later in the string
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Add the current character
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna