class MyQueue:

    def __init__(self):
        # Initialize two empty lists to act as stacks
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # Always push elements onto the input stack
        self.s1.append(x)

    def pop(self) -> int:
        # Ensure s2 has elements to pop from
        self._move_elements()
        return self.s2.pop()

    def peek(self) -> int:
        # Ensure s2 has elements to look at
        self._move_elements()
        return self.s2[-1]

    def empty(self) -> bool:
        # Queue is empty only if both stacks are empty
        return not self.s1 and not self.s2

    def _move_elements(self) -> None:
        # Helper method to transfer elements if output stack is empty
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna