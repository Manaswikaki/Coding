class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            # Process potential collisions for a left-moving asteroid
            while stack and ast < 0 < stack[-1]:
                # If the top right-moving asteroid is smaller, it explodes
                if stack[-1] < abs(ast):
                    stack.pop()
                    continue
                # If they are the same size, both explode
                elif stack[-1] == abs(ast):
                    stack.pop()
                # The current incoming asteroid is destroyed, stop checking
                break
            else:
                # If no collision happens, or all right-moving ones exploded
                stack.append(ast)
                
        return stack


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna