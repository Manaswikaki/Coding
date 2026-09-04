class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, index):
            # Base case: if all characters are successfully matched
            if index == len(word):
                return True
                
            # Boundary checks and character mismatch check
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != word[index]):
                return False
            
            # Temporarily mark the cell as visited by modifying it
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore all 4 adjacent directions (up, down, left, right)
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Backtrack: restore the original character
            board[r][c] = temp
            
            return found

        # Traverse every cell in the grid to find a starting match
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna