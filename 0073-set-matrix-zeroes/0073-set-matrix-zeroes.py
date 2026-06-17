class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False
        col_zero = False

        # 1. Determine if first row/col need to be zeroed
        for i in range(rows):
            if matrix[i][0] == 0:
                col_zero = True
        for j in range(cols):
            if matrix[0][j] == 0:
                row_zero = True

        # 2. Use first row/col as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3. Zero out cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4. Finalize first row and column
        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0
        if row_zero:
            for j in range(cols):
                matrix[0][j] = 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna