class StockSpanner:

    def __init__(self):
        # Stack stores tuples of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # Pop elements from stack while they are less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
            
        # Push current price and its accumulated span onto the stack
        self.stack.append((price, span))
        
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna