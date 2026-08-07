class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # Pop elements from stack if the current digit is smaller 
            # than the top of the stack and we still have k removals left
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k is still greater than 0, remove digits from the end
        if k > 0:
            stack = stack[:-k]
            
        # Join the stack and strip leading zeros
        result = "".join(stack).lstrip('0')
        
        # Return "0" if the string is empty, otherwise return the result
        return result if result else "0"


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna