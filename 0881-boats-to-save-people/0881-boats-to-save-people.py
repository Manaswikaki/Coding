class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort people by their weight
        people.sort()
        
        left = 0
        right = len(people) - 1
        boats = 0
        
        while left <= right:
            # If the lightest and heaviest person can fit together
            if people[left] + people[right] <= limit:
                left += 1  # Lightest person gets on the boat
                
            # The heaviest person always gets on a boat
            right -= 1
            boats += 1  # Increment boat count
            
        return boats


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna