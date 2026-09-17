class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        
        # Iterate from the second row down to the last row
        for r in range(1, n):
            for c in range(n):
                # Fetch top-left, top, and top-right values with boundary handling
                left_diag = matrix[r-1][c-1] if c > 0 else float('inf')
                above = matrix[r-1][c]
                right_diag = matrix[r-1][c+1] if c < n - 1 else float('inf')
                
                # Update current cell with the minimum falling sum path to this point
                matrix[r][c] += min(left_diag, above, right_diag)
                
        # The answer is the minimum value in the final row
        return min(matrix[-1])


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna