class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1  # 1 for positive, -1 for negative

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-":
                res += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                # Push the current result and sign to the stack
                stack.append(res)
                stack.append(sign)
                # Reset result and sign for the new scope
                res = 0
                sign = 1
            elif char == ")":
                res += sign * num
                num = 0
                # Apply the sign and add the result from before the '('
                res *= stack.pop()  # Pop the sign
                res += stack.pop()  # Pop the previous result
                
        return res + (sign * num)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna