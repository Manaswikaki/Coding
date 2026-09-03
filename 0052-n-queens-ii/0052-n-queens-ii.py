class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diag1, diag2):
            # Base case: If all rows are filled, a valid solution is found
            if row == n:
                return 1
            
            count = 0
            
            # Combine all constraints to find attacked positions. 
            # Invert bits to find available spots, and mask to only consider the first 'n' bits.
            available_positions = ~(cols | diag1 | diag2) & ((1 << n) - 1)
            
            while available_positions:
                # Extract the lowest set bit (the next available column)
                position = available_positions & -available_positions
                
                # Remove this position from available pool
                available_positions -= position
                
                # Move to the next row with updated constraints
                count += backtrack(
                    row + 1,
                    cols | position,
                    (diag1 | position) << 1,
                    (diag2 | position) >> 1
                )
                
            return count

        return backtrack(0, 0, 0, 0)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna