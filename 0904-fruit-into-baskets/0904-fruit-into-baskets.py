from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Hash map to store the count of each fruit type in the current window
        basket = {}
        left = 0
        max_fruits = 0
        
        # Expand the window using the right pointer
        for right in range(len(fruits)):
            current_fruit = fruits[right]
            basket[current_fruit] = basket.get(current_fruit, 0) + 1
            
            # If we have more than 2 types of fruits, shrink the window from the left
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                
                # Remove the fruit type entirely if its count drops to 0
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                
                # Move the left pointer forward
                left += 1
            
            # Update the maximum number of fruits collected so far
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna