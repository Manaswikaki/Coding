from collections import deque

class MyStack:

    def __init__(self):
        # Initialize a single deque to simulate our queue
        self.queue = deque()

    def push(self, x: int) -> None:
        # Add the element to the back of the queue
        self.queue.append(x)
        
        # Rotate the queue so the new element comes to the front
        # We rotate size - 1 times
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # The front of the queue is now the top of the stack
        return self.queue.popleft()

    def top(self) -> int:
        # Look at the front element without removing it
        return self.queue[0]

    def empty(self) -> bool:
        # Return True if the queue has no elements
        return len(self.queue) == 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna