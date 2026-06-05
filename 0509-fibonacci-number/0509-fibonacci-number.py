class Solution:
    def fib(self, n: int) -> int:
        x=0
        b=1
        for i in range(n):
            x,b=b,x+b
        return x

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna