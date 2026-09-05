class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        n = len(maze)
        ans = []

        # Base case: if the start or end cell is blocked, no path is possible
        if maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return ans

        # Keep track of visited cells to avoid cycles
        visited = [[False] * n for _ in range(n)]

        # Directions in lexicographical order: 'D' < 'L' < 'R' < 'U'
        directions = [
            (1, 0, 'D'),   # Down
            (0, -1, 'L'),  # Left
            (0, 1, 'R'),   # Right
            (-1, 0, 'U')   # Up
        ]

        def backtrack(r, c, current_path):
            # Destination reached: save the current path
            if r == n - 1 and c == n - 1:
                ans.append("".join(current_path))
                return

            # Mark the current cell as visited
            visited[r][c] = True

            # Explore all 4 valid directions
            for dr, dc, move in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries, if the cell is open (1), and not visited yet
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and maze[nr][nc] == 1:
                    current_path.append(move)
                    backtrack(nr, nc, current_path)
                    current_path.pop()  # Backtrack step

            # Unmark the current cell for other potential path configurations
            visited[r][c] = False

        # Start backtracking from the top-left corner (0, 0)
        backtrack(0, 0, [])
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna