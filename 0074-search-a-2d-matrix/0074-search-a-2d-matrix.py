class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, (ROWS * COLS) - 1
        
        while low <= high:
            mid = (low + high) // 2
            # Map 1D index to 2D coordinates
            row = mid // COLS
            col = mid % COLS
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna