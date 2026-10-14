from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        # Convert deadends to a set for O(1) lookups
        dead_set = set(deadends)
        
        # Edge case: If the starting position is blocked, we can't move
        if "0000" in dead_set:
            return -1
        
        # Edge case: If the start is already the target
        if "0000" == target:
            return 0
            
        # Initialize BFS queue with (current_combination, current_turns)
        queue = deque([("0000", 0)])
        
        # Track visited combinations to prevent infinite loops
        visited = set(["0000"])
        
        while queue:
            current, turns = queue.popleft()
            
            # Generate all 8 possible next combinations
            for i in range(4):
                digit = int(current[i])
                
                # Turn wheel up (+1) and down (-1) with wrap-around logic
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    neighbor = current[:i] + str(new_digit) + current[i+1:]
                    
                    # Check if we reached the target
                    if neighbor == target:
                        return turns + 1
                    
                    # If neighbor is valid and unvisited, add to queue
                    if neighbor not in dead_set and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, turns + 1))
                        
        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna