import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        # Turn the list into a heap in-place: O(N)
        heapq.heapify(self.heap)
        
        # Keep only the k largest elements
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Push the new value onto the heap
        heapq.heappush(self.heap, val)
        
        # If heap size exceeds k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root of the min-heap is the k-th largest element
        return self.heap[0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna