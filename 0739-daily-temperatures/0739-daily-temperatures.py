class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Pairs of (temperature, index)
        
        for i, t in enumerate(temperatures):
            # Check if current temperature is warmer than the temperature at the top of stack
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                answer[stack_i] = i - stack_i
            
            # Push current temperature and its index to the stack
            stack.append((t, i))
            
        return answer


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna