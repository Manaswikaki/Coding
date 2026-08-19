class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initializes the deque with a maximum size of k.
        """
        self.capacity = k
        self.queue = [0] * k
        self.size = 0
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
        """
        if self.isFull():
            return False
        
        # Move front pointer counter-clockwise
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
        """
        if self.isFull():
            return False
        
        # Insert at current rear pointer, then move rear clockwise
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
        """
        if self.isEmpty():
            return False
        
        # Move front pointer clockwise
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
        """
        if self.isEmpty():
            return False
        
        # Move rear pointer counter-clockwise
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Returns the front item from Deque. Returns -1 if the deque is empty.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        """
        Returns the last item from Deque. Returns -1 if the deque is empty.
        """
        if self.isEmpty():
            return -1
        # Rear points to the next empty slot, so the actual last element is at rear - 1
        return self.queue[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Returns true if the deque is empty, or false otherwise.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Returns true if the deque is full, or false otherwise.
        """
        return self.size == self.capacity


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna