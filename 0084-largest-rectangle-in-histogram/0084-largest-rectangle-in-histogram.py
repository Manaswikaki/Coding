class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # Pairs of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            # Maintain monotonic increasing stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate area with the popped height
                max_area = max(max_area, height * (i - index))
                # The current lower height can extend backwards to the popped index
                start = index
            stack.append((start, h))
            
        # Clear remaining elements in the stack
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
            
        return max_area


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna