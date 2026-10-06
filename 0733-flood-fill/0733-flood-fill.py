class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # Get the color of the starting pixel
        start_color = image[sr][sc]
        
        # If the starting pixel already has the target color, no changes are needed
        if start_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # Check boundaries and if the current pixel matches the starting color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
                return
            
            # Update the color of the current pixel
            image[r][c] = color
            
            # Recursively explore all 4 adjacent directions (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Start the flood fill from the given coordinate
        dfs(sr, sc)
        
        return image


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna