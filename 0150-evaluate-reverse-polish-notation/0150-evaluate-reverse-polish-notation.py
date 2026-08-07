class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # The first popped element is the right-hand operand
                b = stack.pop()
                # The second popped element is the left-hand operand
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # int() division in Python truncates toward zero
                    stack.append(int(a / b))
            else:
                # Token is a valid 32-bit integer
                stack.append(int(token))
                
        return stack[0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna