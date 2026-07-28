class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return
        
        ROWS, COLS = len(matrix), len(matrix[0])
        # Create a prefix sum matrix padded with an extra row and column of 0s
        self.prefix_sum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        # Fill the prefix sum table
        for r in range(ROWS):
            for c in range(COLS):
                self.prefix_sum[r + 1][c + 1] = (
                    matrix[r][c] 
                    + self.prefix_sum[r][c + 1] 
                    + self.prefix_sum[r + 1][c] 
                    - self.prefix_sum[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Calculate the region sum using inclusion-exclusion principle
        return (
            self.prefix_sum[row2 + 1][col2 + 1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row1][col1]
        )


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna