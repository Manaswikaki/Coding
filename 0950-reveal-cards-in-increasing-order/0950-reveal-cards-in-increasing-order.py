from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        # 1. Sort the deck in descending order
        deck.sort(reverse=True)
        
        # 2. Use a double-ended queue to simulate the reverse process
        queue = deque()
        
        for card in deck:
            # If the queue already has cards, move the last item to the front
            if queue:
                queue.appendleft(queue.pop())
            # Place the current largest card at the front
            queue.appendleft(card)
            
        return list(queue)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna