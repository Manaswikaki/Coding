class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Track used digits in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize the tracker with existing numbers
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((r, c))

        def backtrack(cell_idx):
            # If we filled all empty cells, the puzzle is solved
            if cell_idx == len(empty_cells):
                return True
                
            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + (c // 3)

            # Try placing digits '1' through '9'
            for digit in map(str, range(1, 10)):
                if (digit not in rows[r] and 
                    digit not in cols[c] and 
                    digit not in boxes[box_idx]):
                    
                    # Place the digit
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)

                    # Move to the next empty cell
                    if backtrack(cell_idx + 1):
                        return True

                    # Undo choice (backtrack)
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)
            
            return False

        backtrack(0)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna