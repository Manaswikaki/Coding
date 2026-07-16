class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Start at the top-right corner
        row = 0
        col = len(matrix[0]) - 1
        
        # Move across the matrix boundaries
        while row < len(matrix) and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True
            elif current > target:
                # All values below this in the column are larger, move left
                col -= 1
            else:
                # All values to the left in this row are smaller, move down
                row += 1
                
        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna