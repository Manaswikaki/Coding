class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initializes the object with the size of the queue to be k.
        """
        self.size = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Inserts an element into the circular queue. 
        Returns true if the operation is successful.
        """
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.head = 0
            
        # Move tail circularly
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue. 
        Returns true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        # If there's only one element, reset pointers
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            # Move head circularly
            self.head = (self.head + 1) % self.size
            
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Gets the front item from the queue. 
        If the queue is empty, return -1.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Gets the last item from the queue. 
        If the queue is empty, return -1.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.size


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna